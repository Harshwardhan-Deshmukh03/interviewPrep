document.addEventListener('DOMContentLoaded', function () {
    const codeArea = document.querySelector('.code-area');
    const outputArea = document.querySelector('.output');
    const inputArea = document.querySelector('.input');
    const runButton = document.querySelector('.btn-run');
    const toggleModeButton = document.querySelector('.toggle-mode');

    runButton.addEventListener('click', function () {
        // Simulate running the code (Example: just echoing the input)
        outputArea.textContent = inputArea.value;
        // Syntax highlighting
        hljs.highlightBlock(outputArea);
    });

    toggleModeButton.addEventListener('click', function () {
        document.body.classList.toggle('dark-mode');
    });

    // Initial syntax highlighting
    hljs.highlightBlock(codeArea);
});
