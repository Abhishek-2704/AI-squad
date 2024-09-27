document.getElementById('file-upload').addEventListener('change', previewImage);
document.getElementById('process-btn').addEventListener('click', processImage);

function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const imagePreview = document.getElementById('image-preview');
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}

function processImage() {
    const fileInput = document.getElementById('file-upload');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please upload an image first.');
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    // Simulate API call for handwritten text recognition
    // Replace this with the actual backend API call
    fetch('https://your-api-endpoint.com/recognize', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const recognizedText = data.recognizedText;
        document.getElementById('recognized-text').textContent = recognizedText;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error processing the image.');
    });
}
fetch('http://127.0.0.1:5000/recognize', {
    method: 'POST',
    body: formData
})
