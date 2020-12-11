// todayDate
today = new Date();

// Get Today Date
var date = today.getDate();

// Get This Month
var thisMonth = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
month = thisMonth[today.getMonth()];

// Get Today Day
var todayDay = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
day = todayDay[today.getDay()];

// Get This Year
var year = today.getFullYear();

// Print Data in HTML
document.getElementById('todayDate').innerHTML = date + " " + month + " " + year + " , " + day;