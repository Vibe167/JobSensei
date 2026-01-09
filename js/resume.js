document.addEventListener('DOMContentLoaded', () => {
    let currentStep = 1;
    const totalSteps = 7;
    let selectedTemplate = null;

    const themeToggle = document.getElementById('themeToggle');
    const isDarkDefault = document.body.classList.contains('dark-theme');
    themeToggle.textContent = isDarkDefault ? '☀️' : '🌙';

    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
        const isDark = document.body.classList.contains('dark-theme');
        themeToggle.textContent = isDark ? '☀️' : '🌙';

        // Refresh preview colors if necessary
        updatePreview();
    });

    const updateProgress = () => {
        const progress = (currentStep / totalSteps) * 100;
        document.getElementById('progressBar').style.width = `${progress}%`;

        document.querySelectorAll('.step').forEach(step => {
            const stepNum = parseInt(step.dataset.step);
            step.classList.toggle('active', stepNum <= currentStep);
        });
    };

    const showStep = (step) => {
        document.querySelectorAll('.form-group').forEach(group => {
            group.classList.remove('active');
        });
        document.querySelector(`.form-group[data-step="${step}"]`).classList.add('active');

        const nextBtn = document.getElementById('nextBtn');
        nextBtn.textContent = step === totalSteps ? 'Finish' : 'Next';

        updateProgress();
    };

    document.getElementById('nextBtn').addEventListener('click', () => {
        if (currentStep < totalSteps) {
            currentStep++;
            showStep(currentStep);
        } else {
            // Handle form submission
            alert('Resume completed! Ready for download.');
        }
    });

    document.getElementById('prevBtn').addEventListener('click', () => {
        if (currentStep > 1) {
            currentStep--;
            showStep(currentStep);
        }
    });

    // Updated skills input handler with improved functionality
    const addSkill = (input, displayElement) => {
        const skillsText = input.value.trim();
        if (!skillsText) return;

        // Clear the input
        input.value = '';

        // Split by commas and add each non-empty skill
        const skillsArray = skillsText.split(',');

        skillsArray.forEach(skill => {
            const trimmedSkill = skill.trim();
            if (trimmedSkill) {
                const chip = document.createElement('span');
                chip.className = 'skill-chip';
                chip.textContent = trimmedSkill;

                // Add delete button
                const deleteBtn = document.createElement('span');
                deleteBtn.innerHTML = '&times;';
                deleteBtn.style.marginLeft = '5px';
                deleteBtn.style.cursor = 'pointer';
                deleteBtn.style.fontWeight = 'bold';
                deleteBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    chip.remove();
                    updatePreview();
                });

                chip.appendChild(deleteBtn);
                displayElement.appendChild(chip);
            }
        });

        updatePreview();
    };

    // Skills input handling
    document.getElementById('skills').addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ',') {
            e.preventDefault();
            addSkill(e.target, document.getElementById('skillsDisplay'));
        }
    });

    // Add "Add" buttons for skills and languages
    const addSkillBtn = document.createElement('button');
    addSkillBtn.type = 'button';
    addSkillBtn.className = 'btn add-btn';
    addSkillBtn.textContent = '+ Add Skills';
    addSkillBtn.addEventListener('click', () => {
        addSkill(document.getElementById('skills'), document.getElementById('skillsDisplay'));
    });

    document.getElementById('skills').insertAdjacentElement('afterend', addSkillBtn);

    // Languages input handling
    document.getElementById('languages').addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ',') {
            e.preventDefault();
            addSkill(e.target, document.getElementById('languagesDisplay'));
        }
    });

    // Add "Add" button for languages
    const addLangBtn = document.createElement('button');
    addLangBtn.type = 'button';
    addLangBtn.className = 'btn add-btn';
    addLangBtn.textContent = '+ Add Languages';
    addLangBtn.addEventListener('click', () => {
        addSkill(document.getElementById('languages'), document.getElementById('languagesDisplay'));
    });

    document.getElementById('languages').insertAdjacentElement('afterend', addLangBtn);

    const updatePreview = () => {
        const preview = document.getElementById('resumePreview');

        // Safely get values with fallbacks
        const safeGetValue = (id) => {
            const element = document.getElementById(id);
            return element ? element.value || '' : '';
        };

        const name = safeGetValue('fullName') || 'Your Name';
        const email = safeGetValue('email') || 'your.email@example.com';
        const phone = safeGetValue('phone') || 'Phone Number';
        const summary = safeGetValue('summary') || 'Professional Summary';

        const templateClass = selectedTemplate || 'modern';

        // Collect skills and languages
        const skillsDisplay = document.getElementById('skillsDisplay');
        const languagesDisplay = document.getElementById('languagesDisplay');
        const skills = Array.from(skillsDisplay.children).map(chip => chip.textContent.replace('×', '').trim()).join(', ');
        const languages = Array.from(languagesDisplay.children).map(chip => chip.textContent.replace('×', '').trim()).join(', ');

        // Properly collect initial education fields
        let educationEntries = [];
        const initialEducation = document.getElementById('educationFields');
        if (initialEducation) {
            // First handle the initial education inputs that aren't in a container div
            const inputs = initialEducation.querySelectorAll(':scope > input');
            const textarea = initialEducation.querySelector(':scope > textarea');

            if (inputs.length >= 3) { // Make sure there are enough inputs to extract values
                const dateInputs = initialEducation.querySelectorAll('.date-range input');
                educationEntries.push({
                    school: inputs[0]?.value || '',
                    degree: inputs[1]?.value || '',
                    field: inputs[2]?.value || '',
                    startYear: dateInputs[0]?.value || '',
                    endYear: dateInputs[1]?.value || '',
                    achievements: textarea?.value || ''
                });
            }

            // Then handle any additional education entries added with the "Add Education" button
            const additionalEntries = initialEducation.querySelectorAll('.education-entry');
            additionalEntries.forEach(entry => {
                const entryInputs = entry.querySelectorAll('input');
                const entryTextarea = entry.querySelector('textarea');
                const entryDateInputs = entry.querySelectorAll('.date-range input');

                educationEntries.push({
                    school: entryInputs[0]?.value || '',
                    degree: entryInputs[1]?.value || '',
                    field: entryInputs[2]?.value || '',
                    startYear: entryDateInputs[0]?.value || '',
                    endYear: entryDateInputs[1]?.value || '',
                    achievements: entryTextarea?.value || ''
                });
            });
        }

        // Properly collect initial experience fields
        let experienceEntries = [];
        const initialExperience = document.getElementById('experienceFields');
        if (initialExperience) {
            // First handle the initial experience inputs
            const inputs = initialExperience.querySelectorAll(':scope > input');
            const textarea = initialExperience.querySelector(':scope > textarea');
            const dateInputs = initialExperience.querySelectorAll('.date-range input');

            if (inputs.length >= 2) { // Make sure there are enough inputs
                experienceEntries.push({
                    company: inputs[0]?.value || '',
                    position: inputs[1]?.value || '',
                    startDate: dateInputs[0]?.value || '',
                    endDate: dateInputs[1]?.value || '',
                    description: textarea?.value || ''
                });
            }

            // Then handle additional experience entries
            const additionalEntries = initialExperience.querySelectorAll('.experience-entry');
            additionalEntries.forEach(entry => {
                const entryInputs = entry.querySelectorAll('input');
                const entryTextarea = entry.querySelector('textarea');
                const entryDateInputs = entry.querySelectorAll('.date-range input');

                experienceEntries.push({
                    company: entryInputs[0]?.value || '',
                    position: entryInputs[1]?.value || '',
                    startDate: entryDateInputs[0]?.value || '',
                    endDate: entryDateInputs[1]?.value || '',
                    description: entryTextarea?.value || ''
                });
            });
        }

        // Collect projects
        let projects = [];
        const projectFields = document.getElementById('projectFields');
        if (projectFields) {
            // Handle initial project inputs
            const initialInputs = projectFields.querySelectorAll(':scope > input');
            const initialTextarea = projectFields.querySelector(':scope > textarea');

            if (initialInputs.length >= 2) {
                projects.push({
                    name: initialInputs[0]?.value || '',
                    tech: initialInputs[1]?.value || '',
                    description: initialTextarea?.value || ''
                });
            }

            // Handle additional project entries
            const projectEntries = projectFields.querySelectorAll('.project-entry');
            projectEntries.forEach(entry => {
                const entryInputs = entry.querySelectorAll('input');
                const entryTextarea = entry.querySelector('textarea');

                projects.push({
                    name: entryInputs[0]?.value || '',
                    tech: entryInputs[1]?.value || '',
                    description: entryTextarea?.value || ''
                });
            });
        }

        // Build preview HTML - Optimized for single page layout
        preview.innerHTML = `
            <div class="resume-template ${templateClass}">
                <h2 class="resume-name">${name}</h2>
                <p class="resume-contact">${email} | ${phone}</p>
                <hr class="resume-divider">
            
                <div class="resume-summary">
                    <h3>Professional Summary</h3>
                    <p>${summary}</p>
                </div>

                <div class="resume-two-column">
                    <div class="resume-left-column">
                        <h3>Education</h3>
                        ${educationEntries.map(edu => `
                            <div class="education-entry">
                                <h4>${edu.school}</h4>
                                <p>${edu.degree} in ${edu.field}</p>
                                <p>${edu.startYear} - ${edu.endYear}</p>
                                <p>${edu.achievements}</p>
                            </div>
                        `).join('')}
                        
                        <h3>Skills</h3>
                        <p>${skills || 'No skills added yet'}</p>
                        
                        <h3>Programming Languages</h3>
                        <p>${languages || 'No languages added yet'}</p>
                    </div>

                    <div class="resume-right-column">
                        <h3>Work Experience</h3>
                        ${experienceEntries.map(exp => `
                            <div class="experience-entry">
                                <h4>${exp.company}</h4>
                                <p><strong>${exp.position}</strong> | ${exp.startDate} - ${exp.endDate}</p>
                                <p>${exp.description}</p>
                            </div>
                        `).join('')}
                        
                        <h3>Projects</h3>
                        ${projects.map(proj => `
                            <div class="project-item">
                                <h4>${proj.name}</h4>
                                <p><strong>Technologies:</strong> ${proj.tech}</p>
                                <p>${proj.description}</p>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        `;
    };

    // Live preview updates
    document.querySelectorAll('input, textarea').forEach(input => {
        input.addEventListener('input', updatePreview);
    });

    // Template selection
    document.querySelectorAll('.template-card').forEach(card => {
        card.addEventListener('click', () => {
            document.querySelectorAll('.template-card').forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            selectedTemplate = card.dataset.template;
            updatePreview();
        });
    });

    // Add experience fields
    document.getElementById('addExperience').addEventListener('click', () => {
        const experienceFields = document.getElementById('experienceFields');
        const newFields = `
            <div class="experience-entry">
                <input type="text" placeholder="Company Name">
                <input type="text" placeholder="Position">
                <div class="date-range">
                    <input type="text" placeholder="Start Date">
                    <input type="text" placeholder="End Date">
                </div>
                <textarea placeholder="Job Description"></textarea>
            </div>
        `;
        experienceFields.insertAdjacentHTML('beforeend', newFields);

        // Update preview after adding new fields
        document.querySelectorAll('#experienceFields input, #experienceFields textarea').forEach(input => {
            input.addEventListener('input', updatePreview);
        });
    });

    // Add education fields
    document.getElementById('addEducation').addEventListener('click', () => {
        const educationFields = document.getElementById('educationFields');
        const newFields = `
            <div class="education-entry">
                <input type="text" placeholder="School/University Name">
                <input type="text" placeholder="Degree">
                <input type="text" placeholder="Field of Study">
                <div class="date-range">
                    <input type="text" placeholder="Start Year">
                    <input type="text" placeholder="End Year (or Expected)">
                </div>
                <textarea placeholder="Academic Achievements & Activities"></textarea>
            </div>
        `;
        educationFields.insertAdjacentHTML('beforeend', newFields);

        // Add event listeners to new education fields
        const newEntry = educationFields.lastElementChild;
        newEntry.querySelectorAll('input, textarea').forEach(input => {
            input.addEventListener('input', updatePreview);
        });
    });

    // Add project fields
    document.getElementById('addProject').addEventListener('click', () => {
        const projectFields = document.getElementById('projectFields');
        const newFields = `
            <div class="project-entry">
                <input type="text" placeholder="Project Name">
                <input type="text" placeholder="Technologies Used">
                <textarea placeholder="Project Description"></textarea>
            </div>
        `;
        projectFields.insertAdjacentHTML('beforeend', newFields);

        // Add event listeners to new fields
        const newEntry = projectFields.lastElementChild;
        newEntry.querySelectorAll('input, textarea').forEach(input => {
            input.addEventListener('input', updatePreview);
        });
    });

    document.getElementById('analyzeBtn').addEventListener('click', () => {
        const aiSuggestions = document.getElementById('aiSuggestions');
        const formData = collectFormData();
        let atsScore = calculateATSScore(formData);

        // Update AI suggestions
        aiSuggestions.innerHTML = `
            <div class="suggestion-card">
                <h3>ATS Score: ${atsScore}%</h3>
                <p>Your resume's compatibility with Applicant Tracking Systems</p>
                <ul>
                    <li>Add more quantifiable achievements in your experience section</li>
                    <li>Consider adding relevant certifications</li>
                    <li>Expand your project descriptions with specific outcomes</li>
                    <li>Include more industry-specific keywords</li>
                </ul>
            </div>
            <div class="suggestion-card">
                <h3>Template Suggestions</h3>
                <p>Based on your experience, the Professional template might better highlight your skills.</p>
            </div>
        `;

        // Auto-navigate to AI suggestions step (now step 7)
        currentStep = 7;
        showStep(currentStep);
    });

    function calculateATSScore(formData) {
        let score = 0;

        try {
            // Check for contact information (20%)
            if (formData.name && formData.name.length > 0) score += 20;

            // Check for sections (80% total)
            if (formData.summary && formData.summary.length > 10) score += 15;
            if (formData.education && formData.education.some(e => e.school && e.degree)) score += 15;
            if (formData.experience && formData.experience.some(e => e.company && e.position)) score += 20;
            if (formData.skills && formData.skills.length > 0) score += 15;
            if (formData.projects && formData.projects.some(p => p.name && p.description)) score += 15;

            return score;
        } catch (error) {
            console.error('Error calculating ATS score:', error);
            return 0;
        }
    }

    function collectFormData() {
        const safeQuerySelector = (parent, selector) => {
            const element = parent.querySelector(selector);
            return element ? element.value || '' : '';
        };

        // Improved data collection for education and experience
        let education = [];
        const educationFields = document.getElementById('educationFields');

        // Collect initial education fields
        const initialEduInputs = educationFields.querySelectorAll(':scope > input');
        const initialEduTextarea = educationFields.querySelector(':scope > textarea');
        const initialEduDateInputs = educationFields.querySelectorAll('.date-range > input');

        if (initialEduInputs.length >= 3) {
            education.push({
                school: initialEduInputs[0].value || '',
                degree: initialEduInputs[1].value || '',
                field: initialEduInputs[2].value || '',
                startYear: initialEduDateInputs[0]?.value || '',
                endYear: initialEduDateInputs[1]?.value || '',
                achievements: initialEduTextarea?.value || ''
            });
        }

        // Collect additional education entries
        educationFields.querySelectorAll('.education-entry').forEach(entry => {
            const inputs = entry.querySelectorAll('input');
            const textarea = entry.querySelector('textarea');
            const dateInputs = entry.querySelectorAll('.date-range input');

            education.push({
                school: inputs[0]?.value || '',
                degree: inputs[1]?.value || '',
                field: inputs[2]?.value || '',
                startYear: dateInputs[0]?.value || '',
                endYear: dateInputs[1]?.value || '',
                achievements: textarea?.value || ''
            });
        });

        // Similar approach for experience and projects
        let experience = [];
        const experienceFields = document.getElementById('experienceFields');

        // Collect initial experience fields
        const initialExpInputs = experienceFields.querySelectorAll(':scope > input');
        const initialExpTextarea = experienceFields.querySelector(':scope > textarea');
        const initialExpDateInputs = experienceFields.querySelectorAll('.date-range > input');

        if (initialExpInputs.length >= 2) {
            experience.push({
                company: initialExpInputs[0].value || '',
                position: initialExpInputs[1].value || '',
                startDate: initialExpDateInputs[0]?.value || '',
                endDate: initialExpDateInputs[1]?.value || '',
                description: initialExpTextarea?.value || ''
            });
        }

        // Collect additional experience entries
        experienceFields.querySelectorAll('.experience-entry').forEach(entry => {
            const inputs = entry.querySelectorAll('input');
            const textarea = entry.querySelector('textarea');
            const dateInputs = entry.querySelectorAll('.date-range input');

            experience.push({
                company: inputs[0]?.value || '',
                position: inputs[1]?.value || '',
                startDate: dateInputs[0]?.value || '',
                endDate: dateInputs[1]?.value || '',
                description: textarea?.value || ''
            });
        });

        let projects = [];
        const projectFields = document.getElementById('projectFields');

        // Collect initial project fields
        const initialProjInputs = projectFields.querySelectorAll(':scope > input');
        const initialProjTextarea = projectFields.querySelector(':scope > textarea');

        if (initialProjInputs.length >= 2) {
            projects.push({
                name: initialProjInputs[0].value || '',
                tech: initialProjInputs[1].value || '',
                description: initialProjTextarea?.value || ''
            });
        }

        // Collect additional project entries
        projectFields.querySelectorAll('.project-entry').forEach(proj => {
            const inputs = proj.querySelectorAll('input');
            const textarea = proj.querySelector('textarea');

            projects.push({
                name: inputs[0]?.value || '',
                tech: inputs[1]?.value || '',
                description: textarea?.value || ''
            });
        });

        // Updated to properly collect skills and languages
        return {
            name: document.getElementById('fullName')?.value || '',
            email: document.getElementById('email')?.value || '',
            phone: document.getElementById('phone')?.value || '',
            summary: document.getElementById('summary')?.value || '',
            education: education,
            experience: experience,
            skills: Array.from(document.querySelectorAll('#skillsDisplay .skill-chip')).map(chip =>
                chip.textContent.replace('×', '').trim()),
            languages: Array.from(document.querySelectorAll('#languagesDisplay .skill-chip')).map(chip =>
                chip.textContent.replace('×', '').trim()),
            projects: projects
        };
    }

    // Download as PDF
   // Optimized Download as PDF
document.getElementById('downloadBtn').addEventListener('click', () => {
    const downloadBtn = document.getElementById('downloadBtn');
    const origText = downloadBtn.textContent;
    downloadBtn.textContent = 'Generating PDF...';
    downloadBtn.disabled = true;

    const previewElement = document.getElementById('resumePreview');

    // 1. Ensure the library is loaded
    if (typeof html2pdf === 'undefined') {
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
        document.body.appendChild(script);
        script.onload = () => generatePDF();
        script.onerror = () => {
            alert('Failed to load PDF library.');
            resetBtn();
        };
    } else {
        generatePDF();
    }

    function resetBtn() {
        downloadBtn.textContent = origText;
        downloadBtn.disabled = false;
    }

    function generatePDF() {
    try {
        // 1. Clone the preview element
        const clonedPreview = previewElement.cloneNode(true);
        
        // 2. STRIP CONTAINER STYLES
        // This removes the black borders/backgrounds captured from the UI container
        clonedPreview.style.background = 'white';
        clonedPreview.style.border = 'none';
        clonedPreview.style.boxShadow = 'none';
        clonedPreview.style.padding = '0';
        clonedPreview.style.margin = '0';
        clonedPreview.classList.remove('dark-theme');

        // 3. TARGET THE RESUME TEMPLATE SPECIFICALLY
        const template = clonedPreview.querySelector('.resume-template');
        if (template) {
            // Force pure white background for the PDF "paper"
            template.style.backgroundColor = 'white';
            template.style.color = 'black';
            template.style.boxShadow = 'none';
            template.style.border = 'none';
            template.style.margin = '0';
            
            // Fix internal entries to be clean for print
            template.querySelectorAll('.experience-entry, .education-entry, .project-item').forEach(entry => {
                entry.style.backgroundColor = 'transparent';
                entry.style.border = 'none';
                entry.style.borderLeft = '2px solid #2563eb';
            });

            // Ensure header text is dark blue/black
            template.querySelectorAll('h1, h2, h3, h4').forEach(h => {
                h.style.setProperty('color', '#1d4ed8', 'important');
            });
        }

        // 4. CLEAN UP CHIPS
        clonedPreview.querySelectorAll('.skill-chip span, .skills-chips span').forEach(el => {
            if (el.textContent.includes('×')) el.remove();
        });

        const name = document.getElementById('fullName')?.value || 'Resume';
        const opt = {
            margin: 0, // Set to 0 to rely on internal template padding
            filename: `${name.replace(/\s+/g, '_')}_Resume.pdf`,
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { 
                scale: 2, 
                useCORS: true, 
                letterRendering: true,
                backgroundColor: '#ffffff' // Force white background for the canvas
            },
            jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
        };

        // 5. Generate PDF from the cleaned template specifically
        // If we generate from 'template' directly instead of 'clonedPreview', 
        // we bypass any outer container borders entirely.
        html2pdf().set(opt).from(template || clonedPreview).save().then(() => {
            resetBtn();
        }).catch(err => {
            console.error(err);
            resetBtn();
        });

    } catch (error) {
        console.error('Error generating PDF:', error);
        resetBtn();
    }
}
});


    // Initialize first step
    showStep(1);
    updatePreview();
});