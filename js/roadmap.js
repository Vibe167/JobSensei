// Roadmap Progress Tracker with Firebase
import { firebaseConfig } from './config.js';
import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js';
import { 
  getAuth, 
  onAuthStateChanged 
} from 'https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js';
import { 
  getFirestore, 
  doc, 
  getDoc, 
  setDoc,
  updateDoc
} from 'https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js';

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

let currentUser = null;
let roadmapProgress = {};

// Auth state listener
onAuthStateChanged(auth, (user) => {
  if (user) {
    currentUser = user;
    loadProgress();
  } else {
    window.location.href = '/pages/login.html';
  }
});

// Load progress from Firebase
async function loadProgress() {
  try {
    const progressRef = doc(db, 'roadmapProgress', currentUser.uid);
    const progressSnap = await getDoc(progressRef);
    
    if (progressSnap.exists()) {
      roadmapProgress = progressSnap.data();
      applyProgress();
    } else {
      // Initialize empty progress
      roadmapProgress = {
        userId: currentUser.uid,
        completedItems: {},
        lastUpdated: new Date().toISOString()
      };
    }
    
    updateProgressStats();
  } catch (error) {
    console.error('Error loading progress:', error);
  }
}

// Apply saved progress to checkboxes
function applyProgress() {
  const completedItems = roadmapProgress.completedItems || {};
  
  Object.keys(completedItems).forEach(itemId => {
    if (completedItems[itemId]) {
      const checkbox = document.querySelector(`[data-item-id="${itemId}"]`);
      if (checkbox) {
        checkbox.checked = true;
        const checklistItem = checkbox.closest('.checklist-item');
        if (checklistItem) {
          checklistItem.classList.add('completed');
        }
      }
    }
  });
  
  updateWeekCompletionStatus();
}

// Save progress to Firebase
async function saveProgress() {
  try {
    const progressRef = doc(db, 'roadmapProgress', currentUser.uid);
    roadmapProgress.lastUpdated = new Date().toISOString();
    
    await setDoc(progressRef, roadmapProgress, { merge: true });
  } catch (error) {
    console.error('Error saving progress:', error);
  }
}

// Initialize checkboxes
function initializeCheckboxes() {
  const checkboxes = document.querySelectorAll('.checkbox-input');
  
  checkboxes.forEach((checkbox, index) => {
    const checklistItem = checkbox.closest('.checklist-item');
    const weekCard = checkbox.closest('.week-card');
    const week = weekCard.dataset.week;
    const phase = weekCard.dataset.phase;
    const type = checklistItem.dataset.type;
    const itemIndex = checklistItem.dataset.index;
    
    // Create unique ID for this item
    const itemId = `phase${phase}_week${week}_${type}${itemIndex}`;
    checkbox.dataset.itemId = itemId;
    
    // Add click handler
    checklistItem.addEventListener('click', (e) => {
      if (e.target !== checkbox) {
        checkbox.checked = !checkbox.checked;
      }
      handleCheckboxChange(checkbox);
    });
    
    checkbox.addEventListener('change', () => {
      handleCheckboxChange(checkbox);
    });
  });
}

// Handle checkbox state change
function handleCheckboxChange(checkbox) {
  const checklistItem = checkbox.closest('.checklist-item');
  const itemId = checkbox.dataset.itemId;
  
  // Update UI
  if (checkbox.checked) {
    checklistItem.classList.add('completed');
  } else {
    checklistItem.classList.remove('completed');
  }
  
  // Update progress data
  if (!roadmapProgress.completedItems) {
    roadmapProgress.completedItems = {};
  }
  roadmapProgress.completedItems[itemId] = checkbox.checked;
  
  // Save to Firebase
  saveProgress();
  
  // Update stats and week status
  updateProgressStats();
  updateWeekCompletionStatus();
}

// Update progress statistics
function updateProgressStats() {
  const allCheckboxes = document.querySelectorAll('.checkbox-input');
  const checkedCheckboxes = document.querySelectorAll('.checkbox-input:checked');
  
  const totalTasks = allCheckboxes.length;
  const completedTasks = checkedCheckboxes.length;
  const percentage = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;
  
  // Update stat cards
  document.getElementById('completedTasks').textContent = completedTasks;
  document.getElementById('totalTasks').textContent = totalTasks;
  document.getElementById('completionPercentage').textContent = `${percentage}%`;
  
  // Update progress bar
  document.getElementById('progressBarFill').style.width = `${percentage}%`;
  
  // Update phase progress
  updatePhaseProgress();
}

// Update phase-specific progress
function updatePhaseProgress() {
  const phases = document.querySelectorAll('.phase-card');
  
  phases.forEach(phase => {
    const phaseIndex = phase.dataset.phaseIndex;
    const phaseCheckboxes = phase.querySelectorAll('.checkbox-input');
    const phaseChecked = phase.querySelectorAll('.checkbox-input:checked');
    
    const phaseTotal = phaseCheckboxes.length;
    const phaseCompleted = phaseChecked.length;
    
    const progressElement = phase.querySelector(`[data-phase-progress="${phaseIndex}"]`);
    if (progressElement) {
      progressElement.textContent = `${phaseCompleted}/${phaseTotal} completed`;
    }
  });
}

// Update week completion status
function updateWeekCompletionStatus() {
  const weekCards = document.querySelectorAll('.week-card');
  
  weekCards.forEach(weekCard => {
    const weekCheckboxes = weekCard.querySelectorAll('.checkbox-input');
    const weekChecked = weekCard.querySelectorAll('.checkbox-input:checked');
    
    // Mark week as completed if all items are checked
    if (weekCheckboxes.length > 0 && weekCheckboxes.length === weekChecked.length) {
      weekCard.classList.add('completed');
    } else {
      weekCard.classList.remove('completed');
    }
  });
}

// Calculate current week based on start date
function updateCurrentWeek() {
  // This would ideally come from the roadmap data
  // For now, we'll keep it simple
  const currentWeekElement = document.getElementById('currentWeekNum');
  if (currentWeekElement) {
    // You can calculate this based on the start date from the roadmap
    // For now, showing week 1
    currentWeekElement.textContent = '1';
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  initializeCheckboxes();
  updateCurrentWeek();
});

// Export functions for potential external use
export {
  loadProgress,
  saveProgress,
  updateProgressStats
};
