
// Auto-dismiss messages after 5 seconds
setTimeout(function() {
    var alerts = document.querySelectorAll('[role="alert"]');
    alerts.forEach(function(alert) {
        alert.style.display = 'none';
    });
}, 5000);


// JavaScript to toggle the category list on mobile
const toggleBtn = document.getElementById('toggle-btn');
const categoryList = document.getElementById('category-list');

toggleBtn.addEventListener('click', () => {
    categoryList.classList.toggle('hidden'); // Toggle hidden class
});



// geolocation
