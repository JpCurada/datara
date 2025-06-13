document.getElementById('moa-upload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const messageBox = document.getElementById('message-box');
    const messageText = document.getElementById('message-text');

    if (file) {
        if (file.type !== 'application/pdf') {
            messageText.textContent = 'Error: Only PDF files are allowed.';
            messageBox.classList.add('show');
            this.value = ''; // Clear the input
            return;
        }
        if (file.size > 5 * 1024 * 1024) { // 5 MB in bytes
            messageText.textContent = 'Error: File size exceeds 5 MB limit.';
            messageBox.classList.add('show');
            this.value = ''; // Clear the input
            return;
        }
        messageText.textContent = `File selected: ${file.name} (${(file.size / 1024 / 1024).toFixed(2)} MB)`;
        messageBox.classList.add('show');

        // In a real application, you would now upload the file to a server
        console.log('File is valid and ready for upload:', file.name);
    } else {
            messageText.textContent = 'No file selected.';
            messageBox.classList.add('show');
        }
});