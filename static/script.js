document.getElementById('predictForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/predict', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('result').textContent = 
            'Predicted Chance of Admission: ' + (data.prediction * 100).toFixed(2) + '%';
    })
    .catch(() => {
        document.getElementById('result').textContent = 'Error occurred. Please try again.';
    });
});