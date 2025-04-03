function setNewMonth(direction) {
    const urlParams = new URLSearchParams(window.location.search);
    let currentMonth = parseInt(urlParams.get('month')) - 1 ?? new Date().getMonth(); // Months are 0-indexed in JS
    let currentYear = parseInt(urlParams.get('year')) ?? new Date().getFullYear();

    if (currentMonth === 11 && direction === 1) {
        currentMonth = 0;
        currentYear += 1;
    } else if (currentMonth === 0 && direction === -1) {
        currentMonth = 11;
        currentYear -= 1;
    } else {
        currentMonth += direction;
    }

    urlParams.set('month', currentMonth+1);
    urlParams.set('year', currentYear);
    window.location.search = urlParams.toString();
}

(function() {
    const previous = document.querySelector('.mantiplex-previous-month');
    previous.addEventListener('click', function() {
        setNewMonth(-1);
    });
    const next = document.querySelector('.mantiplex-next-month');
    next.addEventListener('click', function() {
        setNewMonth(1);
    });
    console.log("Danylko porosia");
})();