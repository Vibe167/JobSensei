// ATS Resume Analyzer - Improved Logic

let resumeText = '';
let jobDescriptionText = '';

// File upload handling
document.getElementById('uploadBtn').addEventListener('click', () => {
  document.getElementById('resumeFile').click();
});

document.getElementById('resumeFile').addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (file) {
    document.getElementById('fileName').textContent = file.name;
    document.getElementById('analyzeBtn').disabled = false;
  }
});

// Analyze button handler
document.getElementById('analyzeBtn').addEventListener('click', analyzeResume);

// Main analysis function
function analyzeResume() {
  const fileInput = document.getElementById('resumeFile');
  const file = fileInput.files[0];

  if (!file) {
    alert('Please upload a resume first!');
    return;
  }

  jobDescriptionText = document.getElementById('jobDescription').value.toLowerCase();

  // Parse PDF
  const fileReader = new FileReader();
  fileReader.onload = function(event) {
    const pdfData = new Uint8Array(event.target.result);

    if (typeof pdfjsLib === 'undefined') {
      alert('Error: pdf.js library is not loaded!');
      return;
    }

    pdfjsLib.getDocument(pdfData).promise.then(function(pdf) {
      let textContent = '';
      const numPages = pdf.numPages;
      let pagePromises = [];

      for (let pageNum = 1; pageNum <= numPages; pageNum++) {
        pagePromises.push(pdf.getPage(pageNum).then(function(page) {
          return page.getTextContent().then(function(text) {
            let lastY = null;
            text.items.forEach(function(item) {
              // Add line breaks when Y position changes significantly
              if (lastY !== null && Math.abs(item.transform[5] - lastY) > 5) {
                textContent += '\n';
              }
              textContent += item.str + ' ';
              lastY = item.transform[5];
            });
            textContent += '\n'; // Add line break between pages
          });
        }));
      }

      Promise.all(pagePromises).then(function() {
        resumeText = textContent.toLowerCase();
        
        // Debug: Log extracted text
        console.log('=== EXTRACTED TEXT ===');
        console.log('Text length:', textContent.length);
        console.log('First 500 characters:', textContent.substring(0, 500));
        console.log('=====================');
        
        // Store full text for display
        window.fullExtractedText = textContent;
        
        const scores = calculateATSScore(textContent, numPages);
        displayResults(scores);
      });
    });
  };
  
  fileReader.readAsArrayBuffer(file);
}

// Comprehensive ATS scoring function
function calculateATSScore(text, pageCount) {
  const textLower = text.toLowerCase();
  
  // 1. Keywords Match (25 points)
  const keywordsScore = analyzeKeywords(textLower);
  console.log('Keywords Score:', keywordsScore);
  
  // 2. Section Structure (20 points)
  const sectionsScore = analyzeSections(textLower);
  console.log('Sections Score:', sectionsScore);
  
  // 3. Contact Information (15 points)
  const contactScore = analyzeContactInfo(textLower);
  console.log('Contact Score:', contactScore);
  
  // 4. Format Quality (15 points)
  const formatScore = analyzeFormat(text, textLower);
  console.log('Format Score:', formatScore);
  
  // 5. Achievements & Metrics (15 points)
  const achievementsScore = analyzeAchievements(textLower);
  console.log('Achievements Score:', achievementsScore);
  
  // 6. Resume Length (10 points)
  const lengthScore = analyzeLength(text, pageCount);
  console.log('Length Score:', lengthScore);
  
  const overallScore = Math.round(
    keywordsScore + sectionsScore + contactScore + 
    formatScore + achievementsScore + lengthScore
  );
  
  console.log('Overall Score:', overallScore);
  
  return {
    overall: Math.min(overallScore, 100),
    keywords: keywordsScore,
    sections: sectionsScore,
    contact: contactScore,
    format: formatScore,
    achievements: achievementsScore,
    length: lengthScore,
    feedback: generateFeedback({
      keywordsScore, sectionsScore, contactScore, 
      formatScore, achievementsScore, lengthScore
    }, textLower)
  };
}

// 1. Keyword Analysis
function analyzeKeywords(text) {
  let score = 0;
  const foundKeywords = [];
  
  if (jobDescriptionText) {
    // Extract keywords from job description
    const jdKeywords = extractKeywords(jobDescriptionText);
    const matchCount = jdKeywords.filter(keyword => {
      if (text.includes(keyword)) {
        foundKeywords.push(keyword);
        return true;
      }
      return false;
    }).length;
    
    const matchPercentage = (matchCount / Math.max(jdKeywords.length, 1)) * 100;
    score = (matchPercentage / 100) * 25;
    
    // Store found keywords for display
    window.foundKeywords = foundKeywords;
  } else {
    // More comprehensive keyword list with categories
    const techKeywords = [
      'javascript', 'python', 'java', 'react', 'node', 'sql', 'html', 'css',
      'angular', 'vue', 'typescript', 'php', 'ruby', 'c++', 'c#', '.net',
      'mongodb', 'postgresql', 'mysql', 'redis', 'aws', 'azure', 'gcp',
      'docker', 'kubernetes', 'jenkins', 'git', 'github', 'gitlab',
      'rest', 'api', 'graphql', 'microservices', 'agile', 'scrum',
      'testing', 'ci/cd', 'devops', 'linux', 'windows', 'android', 'ios'
    ];
    
    const softSkills = [
      'leadership', 'communication', 'teamwork', 'problem solving',
      'analytical', 'creative', 'management', 'collaboration',
      'presentation', 'negotiation', 'strategic', 'planning'
    ];
    
    const allKeywords = [...techKeywords, ...softSkills];
    
    const matchCount = allKeywords.filter(keyword => {
      if (text.includes(keyword)) {
        foundKeywords.push(keyword);
        return true;
      }
      return false;
    }).length;
    
    // More generous scoring: 5+ keywords = full points
    if (matchCount >= 10) {
      score = 25;
    } else if (matchCount >= 7) {
      score = 20;
    } else if (matchCount >= 5) {
      score = 15;
    } else if (matchCount >= 3) {
      score = 10;
    } else if (matchCount >= 1) {
      score = 5;
    }
    
    window.foundKeywords = foundKeywords;
  }
  
  return Math.min(score, 25);
}

// Extract keywords from job description
function extractKeywords(text) {
  const stopWords = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'is', 'are', 'was', 'were', 'be', 'been', 'being'];
  const words = text.match(/\b\w+\b/g) || [];
  const wordFreq = {};
  
  words.forEach(word => {
    if (word.length > 3 && !stopWords.includes(word)) {
      wordFreq[word] = (wordFreq[word] || 0) + 1;
    }
  });
  
  return Object.entries(wordFreq)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 20)
    .map(([word]) => word);
}

// 2. Section Structure Analysis
function analyzeSections(text) {
  const requiredSections = [
    { name: 'experience', patterns: ['experience', 'work history', 'employment', 'professional experience'] },
    { name: 'education', patterns: ['education', 'academic', 'degree', 'university', 'college'] },
    { name: 'skills', patterns: ['skills', 'technical skills', 'competencies', 'expertise'] },
    { name: 'summary', patterns: ['summary', 'profile', 'objective', 'about'] }
  ];
  
  let foundSections = 0;
  window.missingSections = [];
  
  requiredSections.forEach(section => {
    const found = section.patterns.some(pattern => text.includes(pattern));
    if (found) {
      foundSections++;
    } else {
      window.missingSections.push(section.name);
    }
  });
  
  return (foundSections / requiredSections.length) * 20;
}

// 3. Contact Information Analysis
function analyzeContactInfo(text) {
  let score = 0;
  window.contactIssues = [];
  
  // Email
  if (/[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}/i.test(text)) {
    score += 5;
  } else {
    window.contactIssues.push('email');
  }
  
  // Phone
  if (/(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}/.test(text)) {
    score += 5;
  } else {
    window.contactIssues.push('phone');
  }
  
  // LinkedIn or professional link
  if (/linkedin|github|portfolio|website/.test(text)) {
    score += 5;
  } else {
    window.contactIssues.push('professional links');
  }
  
  return score;
}

// 4. Format Quality Analysis
function analyzeFormat(text, textLower) {
  let score = 15;
  window.formatIssues = [];
  
  // Check for problematic formatting
  if (text.length < 300) {
    score -= 5;
    window.formatIssues.push('Resume appears too short or poorly parsed');
  }
  
  // Check for bullet points or structured content (more lenient)
  const hasBullets = text.includes('•') || text.includes('◦') || text.includes('▪');
  const hasDashes = (text.match(/-/g) || []).length > 5;
  const hasAsterisks = (text.match(/\*/g) || []).length > 3;
  
  if (!hasBullets && !hasDashes && !hasAsterisks) {
    score -= 2;
    window.formatIssues.push('Consider using bullet points for better readability');
  }
  
  // Check for excessive special characters (more lenient threshold)
  const specialCharCount = (text.match(/[^\w\s.,;:()\-]/g) || []).length;
  if (specialCharCount > text.length * 0.1) {
    score -= 3;
    window.formatIssues.push('Too many special characters - simplify formatting');
  }
  
  // Check for dates (indicates experience timeline)
  const hasYears = /\b(19|20)\d{2}\b/.test(text);
  if (!hasYears) {
    score -= 2;
    window.formatIssues.push('Include dates for experience and education');
  }
  
  return Math.max(score, 0);
}

// 5. Achievements & Metrics Analysis
function analyzeAchievements(text) {
  let score = 0;
  window.achievementIssues = [];
  
  // Check for numbers/metrics
  const numberMatches = text.match(/\d+%|\d+\+|increased|decreased|improved|reduced|grew|generated|\$\d+/g) || [];
  if (numberMatches.length >= 5) {
    score += 8;
  } else if (numberMatches.length >= 2) {
    score += 4;
  } else {
    window.achievementIssues.push('Add quantifiable achievements with numbers and metrics');
  }
  
  // Check for action verbs
  const actionVerbs = [
    'led', 'managed', 'developed', 'created', 'implemented', 'designed',
    'built', 'improved', 'increased', 'reduced', 'achieved', 'delivered',
    'launched', 'optimized', 'streamlined', 'coordinated'
  ];
  
  const verbCount = actionVerbs.filter(verb => text.includes(verb)).length;
  if (verbCount >= 8) {
    score += 7;
  } else if (verbCount >= 4) {
    score += 4;
  } else {
    window.achievementIssues.push('Use more strong action verbs to start bullet points');
  }
  
  return score;
}

// 6. Resume Length Analysis
function analyzeLength(text, pageCount) {
  const wordCount = text.split(/\s+/).length;
  
  // Optimal: 400-800 words (1-2 pages)
  if (wordCount >= 400 && wordCount <= 800 && pageCount <= 2) {
    return 10;
  } else if (wordCount >= 300 && wordCount <= 1000) {
    return 7;
  } else if (wordCount < 300) {
    window.lengthIssue = 'Resume is too short - add more details about your experience';
    return 3;
  } else {
    window.lengthIssue = 'Resume is too long - keep it concise (1-2 pages)';
    return 5;
  }
}

// Generate detailed feedback
function generateFeedback(scores, text) {
  const feedback = [];
  
  // Keywords feedback
  if (scores.keywordsScore >= 20) {
    feedback.push({
      type: 'success',
      title: 'Excellent Keyword Match',
      message: 'Your resume contains relevant keywords that match well with requirements.'
    });
  } else if (scores.keywordsScore >= 12) {
    feedback.push({
      type: 'warning',
      title: 'Good Keyword Match',
      message: 'Consider adding more relevant keywords from the job description naturally throughout your resume.'
    });
  } else {
    feedback.push({
      type: 'error',
      title: 'Improve Keyword Match',
      message: jobDescriptionText ? 'Add more keywords from the job description to improve ATS compatibility.' : 'Paste a job description above to get specific keyword recommendations.'
    });
  }
  
  // Sections feedback
  if (scores.sectionsScore >= 15) {
    feedback.push({
      type: 'success',
      title: 'Well-Structured Resume',
      message: 'Your resume has all the essential sections ATS systems look for.'
    });
  } else {
    const missing = window.missingSections.join(', ');
    feedback.push({
      type: 'error',
      title: 'Missing Key Sections',
      message: `Add these sections: ${missing}. ATS systems scan for standard section headers.`
    });
  }
  
  // Contact info feedback
  if (scores.contactScore >= 12) {
    feedback.push({
      type: 'success',
      title: 'Complete Contact Information',
      message: 'All essential contact details are present.'
    });
  } else {
    const missing = window.contactIssues.join(', ');
    feedback.push({
      type: 'warning',
      title: 'Incomplete Contact Info',
      message: `Add or verify: ${missing}. Make it easy for recruiters to reach you.`
    });
  }
  
  // Format feedback
  if (scores.formatScore >= 12) {
    feedback.push({
      type: 'success',
      title: 'ATS-Friendly Format',
      message: 'Your resume format is clean and ATS-compatible.'
    });
  } else if (window.formatIssues.length > 0) {
    feedback.push({
      type: 'warning',
      title: 'Format Improvements Needed',
      message: window.formatIssues[0]
    });
  }
  
  // Achievements feedback
  if (scores.achievementsScore >= 12) {
    feedback.push({
      type: 'success',
      title: 'Strong Achievement Focus',
      message: 'Great use of metrics and action verbs to demonstrate impact.'
    });
  } else {
    const issue = window.achievementIssues[0] || 'Add more quantifiable achievements';
    feedback.push({
      type: 'warning',
      title: 'Strengthen Your Achievements',
      message: issue
    });
  }
  
  // Length feedback
  if (scores.lengthScore >= 8) {
    feedback.push({
      type: 'success',
      title: 'Optimal Resume Length',
      message: 'Your resume length is appropriate for ATS systems.'
    });
  } else if (window.lengthIssue) {
    feedback.push({
      type: 'warning',
      title: 'Resume Length Issue',
      message: window.lengthIssue
    });
  }
  
  return feedback;
}


// Display results with animations
function displayResults(scores) {
  const resultsSection = document.getElementById('resultsSection');
  resultsSection.style.display = 'grid';
  
  // Scroll to results
  resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  
  // Animate overall score
  setTimeout(() => {
    animateScore(scores.overall);
    updateScoreStatus(scores.overall);
  }, 300);
  
  // Animate breakdown scores
  setTimeout(() => {
    updateBreakdownScore('keywords', scores.keywords, 25);
    updateBreakdownScore('sections', scores.sections, 20);
    updateBreakdownScore('contact', scores.contact, 15);
    updateBreakdownScore('format', scores.format, 15);
    updateBreakdownScore('achievements', scores.achievements, 15);
    updateBreakdownScore('length', scores.length, 10);
  }, 800);
  
  // Display feedback
  setTimeout(() => {
    displayFeedback(scores.feedback);
  }, 1200);
  
  // Display keywords if found
  if (window.foundKeywords && window.foundKeywords.length > 0) {
    setTimeout(() => {
      displayKeywords(window.foundKeywords);
    }, 1500);
  }
  
  // Display extracted text for debugging
  setTimeout(() => {
    displayExtractedText();
  }, 1800);
}

// Animate circular score
function animateScore(score) {
  const scoreElement = document.getElementById('overallScore');
  const progressCircle = document.getElementById('scoreRingProgress');
  const circumference = 2 * Math.PI * 70;
  const offset = circumference - (score / 100) * circumference;
  
  // Animate number
  let current = 0;
  const increment = score / 50;
  const timer = setInterval(() => {
    current += increment;
    if (current >= score) {
      current = score;
      clearInterval(timer);
    }
    scoreElement.textContent = Math.round(current);
  }, 20);
  
  // Animate circle
  progressCircle.style.strokeDashoffset = offset;
  
  // Change color based on score
  if (score >= 80) {
    progressCircle.style.stroke = '#10b981';
  } else if (score >= 60) {
    progressCircle.style.stroke = '#3b82f6';
  } else if (score >= 40) {
    progressCircle.style.stroke = '#f59e0b';
  } else {
    progressCircle.style.stroke = '#ef4444';
  }
}

// Update score status text
function updateScoreStatus(score) {
  const statusElement = document.getElementById('scoreStatus');
  
  if (score >= 80) {
    statusElement.textContent = 'Excellent - ATS Ready!';
    statusElement.className = 'score-status excellent';
  } else if (score >= 60) {
    statusElement.textContent = 'Good - Minor Improvements Needed';
    statusElement.className = 'score-status good';
  } else if (score >= 40) {
    statusElement.textContent = 'Fair - Needs Improvement';
    statusElement.className = 'score-status fair';
  } else {
    statusElement.textContent = 'Poor - Major Revisions Required';
    statusElement.className = 'score-status poor';
  }
}

// Update individual breakdown scores
function updateBreakdownScore(category, score, maxScore) {
  const percentage = Math.round((score / maxScore) * 100);
  const scoreElement = document.getElementById(`${category}Score`);
  const progressElement = document.getElementById(`${category}Progress`);
  
  scoreElement.textContent = `${percentage}%`;
  
  setTimeout(() => {
    progressElement.style.width = `${percentage}%`;
  }, 100);
}

// Display feedback items
function displayFeedback(feedbackItems) {
  const feedbackList = document.getElementById('feedbackList');
  feedbackList.innerHTML = '';
  
  feedbackItems.forEach((item, index) => {
    setTimeout(() => {
      const feedbackItem = document.createElement('div');
      feedbackItem.className = `feedback-item ${item.type}`;
      
      let icon = 'fa-check-circle';
      if (item.type === 'warning') icon = 'fa-exclamation-triangle';
      if (item.type === 'error') icon = 'fa-times-circle';
      
      feedbackItem.innerHTML = `
        <i class="fas ${icon}"></i>
        <div class="feedback-text">
          <strong>${item.title}</strong>
          <p>${item.message}</p>
        </div>
      `;
      
      feedbackList.appendChild(feedbackItem);
    }, index * 150);
  });
}

// Display found keywords
function displayKeywords(keywords) {
  const keywordsSection = document.getElementById('keywordsSection');
  const keywordsList = document.getElementById('keywordsList');
  
  keywordsList.innerHTML = '';
  keywords.forEach((keyword, index) => {
    setTimeout(() => {
      const tag = document.createElement('span');
      tag.className = 'keyword-tag';
      tag.textContent = keyword;
      keywordsList.appendChild(tag);
    }, index * 50);
  });
  
  keywordsSection.style.display = 'block';
}


// Display extracted text for debugging
function displayExtractedText() {
  const extractedTextSection = document.getElementById('extractedTextSection');
  const extractedTextPreview = document.getElementById('extractedTextPreview');
  const toggleBtn = document.getElementById('toggleFullText');
  
  if (window.fullExtractedText) {
    extractedTextSection.style.display = 'block';
    
    let showingFull = false;
    extractedTextPreview.textContent = window.fullExtractedText.substring(0, 1000) + '...';
    
    toggleBtn.addEventListener('click', () => {
      showingFull = !showingFull;
      if (showingFull) {
        extractedTextPreview.textContent = window.fullExtractedText;
        toggleBtn.textContent = 'Show Preview Only';
      } else {
        extractedTextPreview.textContent = window.fullExtractedText.substring(0, 1000) + '...';
        toggleBtn.textContent = 'Show Full Text';
      }
    });
  }
}
