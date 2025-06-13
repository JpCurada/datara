// Step loader functionality
class StepLoader {
    constructor() {
        this.currentStep = 1;
        this.totalSteps = 7;
        this.stepFiles = {
            1: '[S]Step1.html',
            2: '[S]Step2.html',
            3: '[S]Step3.html',
            4: '[S]Step4.html',
            5: '[S]Step5.html',
            6: '[S]Step6.html',
            7: '[S]Step7.html'
        };
        this.loadedSteps = {};
        this.init();
    }

    async init() {
        await this.loadStep(1);
        this.bindEvents();
        this.updateNavigation();
    }

    async loadStep(stepNumber) {
        if (this.loadedSteps[stepNumber]) {
            this.showStep(stepNumber);
            return;
        }

        try {
            const response = await fetch(this.stepFiles[stepNumber]);
            const html = await response.text();
            
            const container = document.getElementById('form-container');
            container.insertAdjacentHTML('beforeend', html);
            
            this.loadedSteps[stepNumber] = true;
            this.showStep(stepNumber);
        } catch (error) {
            console.error(`Error loading step ${stepNumber}:`, error);
        }
    }

    showStep(stepNumber) {
        // Hide all steps
        document.querySelectorAll('.step-content').forEach(step => {
            step.classList.remove('active');
        });

        // Show current step
        const currentStepElement = document.getElementById(`step-${stepNumber}`);
        if (currentStepElement) {
            currentStepElement.classList.add('active');
        }

        // Update navigation
        document.querySelectorAll('.step-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        const activeBtn = document.querySelector(`[data-step="${stepNumber}"]`);
        if (activeBtn) {
            activeBtn.classList.add('active');
        }

        this.currentStep = stepNumber;
        this.updateNavigation();
    }

    bindEvents() {
        // Step buttons
        const stepButtons = document.querySelectorAll('.step-btn');
        stepButtons.forEach(btn => {
            btn.addEventListener('click', async (e) => {
                const step = parseInt(e.target.dataset.step);
                await this.goToStep(step);
            });
        });
    }

    async goToStep(stepNumber) {
        if (stepNumber < 1 || stepNumber > this.totalSteps) return;
        
        if (!this.loadedSteps[stepNumber]) {
            await this.loadStep(stepNumber);
        } else {
            this.showStep(stepNumber);
        }
    }

    updateNavigation() {
        const backBtn = document.getElementById('back-btn');
        const nextBtn = document.getElementById('next-btn');
        const submitBtn = document.getElementById('submit-btn');

        // Hide back button on first step
        if (this.currentStep === 1) {
            backBtn.style.display = 'none';
        } else {
            backBtn.style.display = 'inline-block';
        }

        // Show submit button on last step
        if (this.currentStep === this.totalSteps) {
            nextBtn.style.display = 'none';
            submitBtn.style.display = 'inline-block';
        } else {
            nextBtn.style.display = 'inline-block';
            submitBtn.style.display = 'none';
        }
    }

    async nextStep() {
        if (this.currentStep < this.totalSteps) {
            await this.goToStep(this.currentStep + 1);
        }
    }

    async previousStep() {
        if (this.currentStep > 1) {
            await this.goToStep(this.currentStep - 1);
        }
    }
}

// Global step loader instance
window.stepLoader = new StepLoader();
