document.addEventListener("DOMContentLoaded", function() {
    const toggleModeButton = document.querySelector('.toggle-mode');
    const body = document.body;

    // Check if dark mode preference is already set
    const isDarkMode = localStorage.getItem('darkMode') === 'true';

    // Set initial mode based on preference
    if (isDarkMode) {
        enableDarkMode();
    }

    // Toggle dark mode
    toggleModeButton.addEventListener('click', function() {
        if (isDarkMode) {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    });

    function enableDarkMode() {
        body.classList.add('dark-mode');
        localStorage.setItem('darkMode', 'true');
        isDarkMode = true;
    }

    function disableDarkMode() {
        body.classList.remove('dark-mode');
        localStorage.setItem('darkMode', 'false');
        isDarkMode = false;
    }
});
