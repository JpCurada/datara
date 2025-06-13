// Form validation functionality
class FormValidator {
    constructor() {
        this.addValidationListeners();
    }

    validateStep(stepNumber) {
        const currentStepElement = document.getElementById(`step-${stepNumber}`);
        let isValid = true;

        switch (stepNumber) {
            case 1:
                // Validate privacy agreement
                const privacyCheckbox = document.getElementById('privacy-agree');
                if (!privacyCheckbox.checked) {
                    alert('Please agree to the Privacy Policy to continue.');
                    isValid = false;
                }

                // Validate email
                const emailInput = document.getElementById('email');
                if (!emailInput.value.trim()) {
                    alert('Please enter your email address.');
                    emailInput.focus();
                    isValid = false;
                }
                break;

            case 2:
                // Validate required personal information
                const requiredFields = ['first-name', 'last-name', 'birth-day', 'birth-year'];
                for (let fieldId of requiredFields) {
                    const field = document.getElementById(fieldId);
                    if (!field.value.trim()) {
                        alert(`Please fill in the ${field.previousElementSibling.textContent}.`);
                        field.focus();
                        isValid = false;
                        break;
                    }
                }
                break;

            case 3:
                // Address validation
                const streetField = document.getElementById('street');
                const houseNumberField = document.getElementById('house-number');
                if (!streetField.value.trim() && !houseNumberField.value.trim()) {
                    alert('Please provide either street/subdivision or house number information.');
                    streetField.focus();
                    isValid = false;
                }
                break;

            case 5:
                // Validate text areas
                const scholarshipReason = document.getElementById('scholarship-reason');
                const careerGoals = document.getElementById('career-goals');
                
                if (!scholarshipReason.value.trim()) {
                    alert('Please explain why you want this scholarship.');
                    scholarshipReason.focus();
                    isValid = false;
                } else if (!careerGoals.value.trim()) {
                    alert('Please describe your career goals.');
                    careerGoals.focus();
                    isValid = false;
                }
                break;

            case 7:
                // Validate confirmation checkbox
                const confirmCheckbox = document.getElementById('confirm-details');
                if (!confirmCheckbox.checked) {
                    alert('Please confirm that all details provided are true.');
                    isValid = false;
                }
                break;
        }

        return isValid;
    }

    addValidationListeners() {
        // Email validation
        document.addEventListener('change', (e) => {
            if (e.target.id === 'email') {
                if (e.target.value && !e.target.value.includes('@')) {
                    e.target.style.borderColor = '#ef4444';
                } else {
                    e.target.style.borderColor = '#d1d5db';
                }
            }
        });

        // Character count for textareas
        document.addEventListener('input', (e) => {
            if (e.target.tagName === 'TEXTAREA' && e.target.hasAttribute('maxlength')) {
                this.updateCharacterCount(e.target);
            }

            // Auto-format phone numbers
            if (e.target.type === 'tel') {
                e.target.value = this.formatPhoneNumber(e.target.value);
            }
        });

        // Birthday validation
        document.addEventListener('blur', (e) => {
            if (e.target.id === 'birth-year') {
                const year = parseInt(e.target.value);
                const currentYear = new Date().getFullYear();
                
                if (year && (year > currentYear || year < 1900)) {
                    e.target.style.borderColor = '#ef4444';
                    alert('Please enter a valid birth year.');
                } else {
                    e.target.style.borderColor = '#d1d5db';
                }
            }
        });
    }

    updateCharacterCount(textarea) {
        const maxLength = textarea.getAttribute('maxlength');
        const parentDiv = textarea.parentElement;
        
        let counter = parentDiv.querySelector('.character-counter');
        if (!counter) {
            counter = document.createElement('div');
            counter.className = 'character-counter';
            counter.style.fontSize = '12px';
            counter.style.color = '#6b7280';
            counter.style.textAlign = 'right';
            counter.style.marginTop = '5px';
            parentDiv.appendChild(counter);
        }
        
        const remaining = maxLength - textarea.value.length;
        counter.textContent = `${remaining} characters remaining`;
        
        if (remaining < 50) {
            counter.style.color = '#ef4444';
        } else {
            counter.style.color = '#6b7280';
        }
    }

    formatPhoneNumber(input) {
        const cleaned = input.replace(/\D/g, '');
        const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
        if (match) {
            return `${match[1]}-${match[2]}-${match[3]}`;
        }
        return input;
    }

    collectFormData() {
        const formData = {};
        
        const inputs = document.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            if (input.type === 'checkbox') {
                if (!formData[input.name]) formData[input.name] = [];
                if (input.checked) formData[input.name].push(input.value);
            } else if (input.type === 'radio') {
                if (input.checked) formData[input.name] = input.value;
            } else {
                formData[input.name] = input.value;
            }
        });
        
        return formData;
    }
}

// Global form validator instance
window.formValidator = new FormValidator();