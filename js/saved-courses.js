// Import Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import {
  getAuth,
  onAuthStateChanged,
  signOut,
} from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";
import {
  getFirestore,
  doc,
  getDoc,
  updateDoc,
  arrayRemove,
} from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";

// Import Firebase configuration from centralized config
import { firebaseConfig } from './config.js';

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// Theme Toggle Functionality
document.addEventListener("DOMContentLoaded", function () {
  const themeToggle = document.getElementById("theme-toggle");
  const html = document.documentElement;

  // Check for saved theme preference
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    html.setAttribute("data-theme", savedTheme);
    updateThemeIcon(savedTheme);
  }

  // Theme toggle click handler
  themeToggle.addEventListener("click", function () {
    const currentTheme = html.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";

    html.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    updateThemeIcon(newTheme);
  });

  // Update theme icon based on current theme
  function updateThemeIcon(theme) {
    const icon = themeToggle.querySelector("i");
    if (theme === "dark") {
      icon.classList.remove("fa-moon");
      icon.classList.add("fa-sun");
    } else {
      icon.classList.remove("fa-sun");
      icon.classList.add("fa-moon");
    }
  }
});

// Check auth state and load saved courses
onAuthStateChanged(auth, async (user) => {
  if (user) {
    await loadSavedCourses();
    
    // Setup logout functionality
    document.getElementById("logoutBtn").addEventListener("click", () => {
      signOut(auth)
        .then(() => {
          alert("Logged out successfully!");
          window.location.href = "/pages/login.html";
        })
        .catch((error) => {
          console.error("Logout error:", error);
        });
    });
  } else {
    // Redirect to login if not authenticated
    window.location.href = "/pages/login.html";
  }
});

// Load saved courses from Firebase
async function loadSavedCourses() {
  const user = auth.currentUser;
  const container = document.getElementById("saved-courses-container");
  
  if (!user) return;
  
  try {
    const userDocRef = doc(db, "users", user.uid);
    const userDoc = await getDoc(userDocRef);
    
    if (userDoc.exists() && userDoc.data().savedCourses) {
      const savedCourses = userDoc.data().savedCourses;
      
      if (savedCourses.length === 0) {
        showEmptyState(container);
      } else {
        renderSavedCourses(savedCourses, container);
      }
    } else {
      showEmptyState(container);
    }
  } catch (error) {
    console.error("Error loading saved courses:", error);
    container.innerHTML = `
      <div class="error-state">
        <p>Error loading your saved courses. Please try again later.</p>
      </div>
    `;
  }
}

// Render saved courses in the container
function renderSavedCourses(courses, container) {
  container.innerHTML = "";
  
  // Sort courses by saved date (newest first)
  courses.sort((a, b) => new Date(b.savedAt) - new Date(a.savedAt));
  
  // Update stats
  updateStats(courses);
  
  courses.forEach(course => {
    const courseType = course.kind.includes("playlist") ? "Playlist" : "Video";
    const savedDate = new Date(course.savedAt).toLocaleDateString();
    
    const courseElement = document.createElement("div");
    courseElement.className = "saved-course-item";
    courseElement.dataset.id = course.id;
    
    courseElement.innerHTML = `
      <div class="course-info">
        <img src="${course.thumbnail}" alt="${course.title}">
        <div class="course-details">
          <h4 class="course-title">${course.title}</h4>
          <span class="course-type">${courseType}</span>
          <span class="course-date">Saved on: ${savedDate}</span>
        </div>
      </div>
      <div class="course-actions">
        <a href="${course.url}" target="_blank" class="view-course-btn">
          <i class="fas fa-external-link-alt"></i> View
        </a>
        <button class="remove-course-btn">
          <i class="fas fa-trash-alt"></i> Remove
        </button>
      </div>
    `;
    
    container.appendChild(courseElement);
    
    // Add event listener to the remove button
    const removeButton = courseElement.querySelector(".remove-course-btn");
    removeButton.addEventListener("click", () => {
      console.log("Remove button clicked for course:", course.id);
      removeSavedCourse(course);
    });
  });
}

// Update stats boxes
function updateStats(courses) {
  const totalCourses = courses.length;
  const playlists = courses.filter(c => c.kind && c.kind.includes("playlist")).length;
  const videos = courses.filter(c => c.kind && c.kind.includes("video")).length;
  
  // Update total courses
  const totalCoursesElement = document.getElementById("total-courses");
  if (totalCoursesElement) {
    totalCoursesElement.textContent = totalCourses;
  }
  
  // Update playlists count
  const totalPlaylistsElement = document.getElementById("total-playlists");
  if (totalPlaylistsElement) {
    totalPlaylistsElement.textContent = playlists;
  }
  
  // Update videos count
  const totalVideosElement = document.getElementById("total-videos");
  if (totalVideosElement) {
    totalVideosElement.textContent = videos;
  }
}

// Show empty state when no courses are saved
function showEmptyState(container) {
  // Update stats to zero
  updateStats([]);
  
  container.innerHTML = `
    <div class="empty-state">
      <i class="fas fa-bookmark"></i>
      <p>You haven't saved any courses yet.</p>
      <p>Find and save courses from your dashboard to access them here.</p>
      <button class="go-to-dashboard" onclick="window.location.href='/pages/dashboard.html'">
        Go to Dashboard
      </button>
    </div>
  `;
}

// Remove a saved course
async function removeSavedCourse(course) {
  const user = auth.currentUser;
  if (!user) return;
  
  if (confirm(`Are you sure you want to remove "${course.title}" from your saved courses?`)) {
    try {
      // Get a reference to the user document
      const userDocRef = doc(db, "users", user.uid);
      
      // Get the current user document
      const userSnapshot = await getDoc(userDocRef);
      
      if (userSnapshot.exists()) {
        // Get the current savedCourses array
        const userData = userSnapshot.data();
        const currentCourses = userData.savedCourses || [];
        
        // Create a new array without the course to remove
        const updatedCourses = currentCourses.filter(c => c.id !== course.id);
        
        // Update the document with the new array
        await updateDoc(userDocRef, {
          savedCourses: updatedCourses
        });
        
        console.log("Course removed successfully!");
        
        // Reload the courses display
        await loadSavedCourses();
      }
    } catch (error) {
      console.error("Error removing course:", error);
      alert("Failed to remove course. Please try again.");
    }
  }
}