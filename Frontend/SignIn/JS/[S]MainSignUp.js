// Main application script
class ApplicationForm {
    constructor() {
        this.init();
    }

    init() {
        this.bindNavigationEvents();
        this.addSmoothScrolling();
    }

    bindNavigationEvents() {
        // Navigation buttons
        document.getElementById('back-btn').addEventListener('click', () => {
            this.previousStep();
        });

        document.getElementById('next-btn').addEventListener('click', () => {
            this.nextStep();
        });

        document.getElementById('submit-btn').addEventListener('click', () => {
            this.submitForm();
        });
    }

    nextStep() {
        if (window.formValidator.validateStep(window.stepLoader.currentStep)) {
            window.stepLoader.nextStep();
        }
    }

    previousStep() {
        window.stepLoader.previousStep();
    }

    submitForm() {
        if (window.formValidator.validateStep(window.stepLoader.currentStep)) {
            const formData = window.formValidator.collectFormData();
            
            alert('Application submitted successfully! Thank you for your submission.');
            console.log('Form Data:', formData);
            
            // In a real application, you would send this data to a server
        }
    }

    addSmoothScrolling() {
        // Auto-scroll to top when changing steps
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('step-btn') || 
                e.target.classList.contains('nav-btn')) {
                setTimeout(() => {
                    window.scrollTo({
                        top: 0,
                        behavior: 'smooth'
                    });
                }, 100);
            }
        });
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ApplicationForm();
});