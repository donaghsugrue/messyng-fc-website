// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
// Assorted shared variables and constants 

// var fs = require("fs");
// var data = readFileSync("basicStore.json");
// var basicStore = JSON.parse(data);


// document.addEventListener("DOMContentLoaded", function() {
//     console.log(basicStore);
// });

const valuesToUpdate = {
    luvCount: 0, // JSOn store
    viewCount: 0 // JSON store
};



// Today's date
const today = new Date();





// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// Random advert JS
// ATM, just randomly selects an advert from a given array and displays it on the page.
// TO DO LIST:
// - advert 2 and 3 are not displaying for some reason? They work if I right click and open in new tab, I thought it was a problem with the ordering of how parts are loaded but advert 2 is hard coded into the html rn and that isn't helping.

const theImages = [
    "static/media/mock_ads/advert1.png",
    "static/media/mock_ads/advert2.png",
    "static/media/mock_ads/advert3.png"
];

document.addEventListener("DOMContentLoaded", function() {

    // Create a variable to store the number of images in the array
    var options = theImages.length;

    // Randomly select the index of which image to be displayed. need to minus 1 when I actually move it over to being an index.
    var whichImage = Math.round(Math.random() * (options));

    // This chooses it from the array. Not using this rn.
    // document.getElementById("advertImg").src =  theImages[whichImage - 1]

    // This writes the src as a string and places that in
    document.getElementById("advertImg").src = "static/media/mock_ads/advert" + String(whichImage) + ".png";

    // Just for testing. Uncomment to always load in advert2.png
    // document.getElementById("advertImg").src = "../static/media/mock_ads/advert2.png";

});





// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// Relationship status
// ATM, just randomly selects a relationship status from the list below and displays it on the page.

const relationshipStatuses = [
    "It's Complicated",
    "Down For Whatever",
    "Single",
    "Married",
    "Taken"
]

document.addEventListener("DOMContentLoaded", function() {

    // Create a variable to store the number of options in the relationshipStatuses array
    var optionsRelationshipStatuses = relationshipStatuses.length;
    
    // Create a variable to store a random number between 0 and the number of options in the relationshipStatuses array. Minus 1 because arrays start at 0
    var randomRelationshipStatusesIndex = Math.round(Math.random() * (optionsRelationshipStatuses - 1));

    // Place this into the html
    document.getElementById("relationship-status").innerHTML = relationshipStatuses[randomRelationshipStatusesIndex];

});





// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// Share The Luv
// Display number of luv clicks received on the page. Also limits clicks to 5 per user per day.
// TO DO LIST:
// - Store the figure in database on page load so that other users also affect it and see it updating.

// Handler to run on page load to add to the html
document.addEventListener("DOMContentLoaded", function() {

    // if luvCount exists in the JSON file, then just add the value to the html
    if (localStorage.luvCount) {
        
        document.getElementById("luv-counter").innerHTML = localStorage.luvCount + " ❤️";
    
    // if luvCount doesn't exist, then create it, set it to 1, and add it to the html.
    // While we're at it, we'll check if luvLimit exists in local storage and if not we'll create it and set it to 5.
    } else {

        if (!localStorage.luvLimit) {

            localStorage.luvLimit = 5;

        }

        console.log("luv count added to JSON file");
        localStorage.luvCount = 1;

        document.getElementById("luv-counter").innerHTML = localStorage.luvCount + " ❤️";

    }

    // Console log for testing
    console.log("Share the luv count", localStorage.luvCount);
    console.log("Share the luv limit", localStorage.luvLimit);
    console.log("Day it was stored", localStorage.luvLimitDay);

});

// handler to increase the count on button click
function incrementClick() {

    //  Define a "today"
    var luvLimitToday = today.getDate();

    // if luvLimitDay isn't in storage then we need to create it
    if (!localStorage.luvLimitDay) {

        // If there isn't a day in storage, then it should be today
        localStorage.luvLimitDay = luvLimitToday;

    }

    // if luvLimit doesn't exist in storage
    if (!localStorage.luvLimit) {

        // create it and set it to 5.
        localStorage.luvLimit = 5;

        // Because button has been clicked we now take one from click limit and add a luv
        localStorage.luvLimit = parseInt(localStorage.luvLimit) - 1;
        localStorage.luvCount = parseInt(localStorage.luvCount) + 1;

    // if luvLimit exists in storage, then check if it's been more than a day since the last time the button was clicked
    } else if (localStorage.luvLimitDay != luvLimitToday) {

        // if it has been more than a day (if the two dates aren't the same), then reset luvLimit to 5
        localStorage.luvLimit = 5;
        
    }

    // Now that limits have been checked and we're sure things are in storage we can process the click properly
    // if user still has spare luvLimit today, then follow the normal button click process
    if (localStorage.luvLimit > 0) {

        // if luvCount exists in storage, then get it, add 1 to it, and reduce luvLimit by 1
        if (localStorage.luvCount) {

            localStorage.luvCount = parseInt(localStorage.luvCount) + 1;

            localStorage.luvLimit = parseInt(localStorage.luvLimit) - 1;
        
        // if luvCount doesn't exist in storage, then create it and set it to 1
        } else {

            localStorage.luvCount = 1;

        }
    
    // Else, user has used their 5 luvLimit for the day, so we'll alert them to that fact
    } else {
        alert("Your daily limits of luv has been met. Come back tomorrow and you can leave 5 more luv.");
    }

    // Console log for testing
    console.log("Share the luv count", localStorage.luvCount);
    console.log("Share the luv limit", localStorage.luvLimit);
    console.log("Day it was stored", localStorage.luvLimitDay);

    // Add to the html
    document.getElementById("luv-counter").innerHTML = localStorage.luvCount + " ❤️";

}





// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// Profile views
// Displays a count of the amount of visitors to the page since it was published.
// Adapted from stack overflow. Basically working but currently using local storage.
// TO DO LIST:
// - Store the figure in database on page load so that other users also affect it and see it updating.

window.addEventListener("load", function() {

    // if viewCount exists in storage
    if (localStorage.viewCount) {

        // get it and add 1 to it
        localStorage.viewCount = parseInt(localStorage.viewCount) + 1;

    // if viewCount doesn't exist in localStorage
    } else {

        // create it and set it to 1
        localStorage.viewCount = 1;

    }
    
    // print to console for testing
    console.log("page view count", localStorage.viewCount);

    // Add to the html
    document.getElementById("profile-views").innerHTML = localStorage.viewCount;

});





// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// Member since
// Trying to list the date this site was first published

document.addEventListener("DOMContentLoaded", function() {

    document.getElementById("member-since").innerHTML = "26/11/2023";

});





// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// Last active
// Show date page was last updated - Trying to list how long ago the last update was made

// Dates will all need to be formatted as follows:
// Within the first hour                =   Less than an hour ago  
// After an hour but before 2 hours     =   n hour ago
// Anywhere between 2 and 23 hours ago  =   n hours ago
// After 24 hours but before 48 hours   =   n day ago
// Anywhere between 2 and 6 days ago    =   n days ago
// After 7 days but before 8 days       =   n week ago
// Anywhere between 1 and 3 weeks ago   =   n weeks ago
// After 4.3 weeks but before           =   n month ago
// Anywhere between 2 and 11 months ago =   n months ago
// Anywhere over 1 year ago             =   01/01/1990

const timeIncrements = [
    "Less than an hour ago",    // 0
    " hour ago",                // 1
    " hours ago",               // 2
    " day ago",                 // 3
    " days ago",                // 4
    " week ago",                // 5
    " weeks ago",               // 6
    " month ago",               // 7
    " months ago",              // 8
    ""                          // 9
]

document.addEventListener("DOMContentLoaded", function() {

    // Empty variable to store string that we will put into the HTML
    let durationAgo;

    // Extract the day of the month, the month as a number (starts w Jan as 0 so adding 1), and the year
    var todayDay = today.getDate();
    var todayMonth = today.getMonth() + 1;
    var todayYear = today.getFullYear();
    var todayHour = today.getHours();

    // Format of last modified is mm/dd/yyyy hh:mm:ss, we want to cut this up into the following variables and also change them to int so that we can do maths with them:
    // var updateDay = parseInt(document.lastModified.substring(3, 4));
    // var updateMonth = parseInt(document.lastModified.substring(0, 1));
    // var updateYear = parseInt(document.lastModified.substring(6, 9));
    // var updateHour = parseInt(document.lastModified.substring(11, 12));

    // Just for testing
    var updateDay = 29;
    var updateMonth = 10;
    var updateYear = 2023;
    var updateHour = 18;

    // Convert the date into a number of days since year 0
    var dayDiff = todayDay - updateDay;
    var monthDiff = todayMonth - updateMonth;
    var yearDiff = todayYear - updateYear;
    var hourDiff = todayHour - updateHour;

    // if yearDiff is more than 1, then it's been more than 1 year since the last update no matter what
    // EG todayYear is 2023 and updateYear is 2020, then yearDiff is 3
    if (yearDiff > 1) {
        durationAgo = updateDay + "/" + updateMonth + "/" + updateYear + " " + timeIncrements[9];

    // if yearDiff is exactly 1, then it's between 1 month and 23 months since the last update, so we must nest an if
    // EG todayYear is 2023 and updateYear is 2022 then yearDiff is 1, but Feb/23 and Oct/22 are only 4 months away from each other
    } else if (yearDiff == 1) {

        // if yearDiff is exactly 1 and todayMonth is before updateMonth, then it's been more than 1 year since the last update no matter what
        // EG todayDate is 07/2023 and updateYear is 02/2022, then yearDiff is 1, monthDiff is 5 
        if (monthDiff > 1) {
            durationAgo = updateDay + "/" + updateMonth + "/" + updateYear + " " + timeIncrements[9];

        // if yearDiff is exactly 1 and monthDiff is more than 1 but less than 11, then it's been less than a year but more than 1 month since the last update
        // EG todayDate is 07/2023 and update is 09/2022, then yearDiff is 1, monthDiff is -2
        } else if (monthDiff > 1) {

            // To make the sum easier we can add 12 to todayMonth, so that we can just subtract updateMonth from it
            todayMonth = todayMonth + 12;
            monthDiff = todayMonth - updateMonth;

            durationAgo = monthDiff + timeIncrements[8];

        // if yearDiff is exactly 1 and monthDiff is exactly 1, then it's might be 1 month since the last update, but it could be less than that so we will nest an if
        // EG todayDate is 07/2023 and update is 06/2022, then yearDiff is 1, monthDiff is 1, but 
        } else if (monthDiff == 1) {

            // if yearDiff is more than 31 days, then it's been more than 1 month but less than 1 year since the last update no matter what
            // EG todayDate is 01/01/2023 and updateYear is 31/12/2022, then yearDiff is 1, monthDiff is 1, dayDiff is -30
            if (dayDiff < 0) {

                // To make the sum easier we can add 31 to todayDay, so that we can just subtract updateDay from it. 31 because this can only happen in Dec to Jan.
                todayDay = todayDay + 31;
                dayDiff = todayDay - updateDay;

                durationAgo = monthDiff + timeIncrements[8];

            // if monthDiff is exactly 1 and the dayDiff is more than 1 but less than 31, then it's been less than a month but more than 1 day since the last update
            } else if (dayDiff > 1) {
                durationAgo = monthDiff + timeIncrements[7];

            // monthDiff is exactly 1 and the dayDiff is exactly 1, then it's might be 1 day since the last update, but it could be less than that so we will nest an if
            } else if (dayDiff == 1) {

                // To make the sum easier we can add 31 to todayDay, so that we can just subtract updateDay from it. 31 because this can only happen in Dec to Jan.
                todayHour = todayHour + 24;
                hourDiff = todayHour - updateHour;

                if (hourDiff > 24) {
                    durationAgo = dayDiff + timeIncrements[3];
                }

                // TEMP TEMP TEMP
                durationAgo = "Hello World!"
            
            // If dayDiff is less than 1, then it's the same month and date but 1 year removed. I don't really care to be that specific so I'll just say it's over a year ago.
            } else {
                durationAgo = updateDay + "/" + updateMonth + "/" + updateYear + " " + timeIncrements[9];
            }

        // if yearDiff is 1 and monthDiff is 0, then it's the same month but 1 year apart so we need to check the days which we will do by nesting an if.
        } else {

            // TEMP TEMP TEMP
            durationAgo = "Hello World!"

        }

    // if yearDiff is 0, then it's definitely between 1 and 11 months ago, so we must nest an if to determine month difference only
    // EG todayYear is 2023 and updateYear is 2023, then yearDiff is 0
    } else {

        // If month diff is greater than 1, then it's been more than 1 month but also must be less than 1 year since the last update no matter what
        // EG todayMonth is 07 and updateMonth is 04, then monthDiff is 3
        if (monthDiff > 1) {

            durationAgo = monthDiff + timeIncrements[8];

        // If yeardiff is 0 and monthdiff is exactly 1, then it's might be 1 month since the last update, but it could be less than that so we will nest an if
        // EG todayMonth is 07 and updateMonth is 06, then monthDiff is 1 but it could be 02/07/2023 and 28/06/2023
        } else if (monthDiff == 1) {

            // If yearDiff is 0, monthDiff is 1, and dayDiff is less than 0 then it's currently the same month
            // EG todayDate is 02/07/2023 and updateDate is 28/06/2023, then yearDiff is 0, monthDiff is 1, and dayDiff is -26
            if (dayDiff < 0) {
                // TEMP TEMP TEMP
                durationAgo = "Hello World!";

            // If yearDiff is 0, monthDiff is 1, and dayDiff more than 1 then it's a few days more than a month since the last update
            // EG todayDate is 02/07/2023 and updateDate is 02/06/2023, then yearDiff is 0, monthDiff is 1, and dayDiff is 0
            } else if (dayDiff > 1) {

            
            // If yearDiff is 0, monthDiff is 1, and dayDiff 0 then it's been exactly 1 month since the last update
            // EG todayDate is 02/07/2023 and updateDate is 02/06/2023, then yearDiff is 0, monthDiff is 1, and dayDiff is 0
            } else if (dayDiff == 1) {
                durationAgo = monthDiff + timeIncrements[7];

            // If yearDiff is 0, monthDiff is 1, and dayDiff 0 then it's been exactly 1 month since the last update
            // EG todayDate is 02/07/2023 and updateDate is 02/06/2023, then yearDiff is 0, monthDiff is 1, and dayDiff is 0
            } else {
                durationAgo = monthDiff + timeIncrements[7];
            }

        // If yeardiff is 0 and month diff is 0, then it's been less than a month since the last update, so we need to check the days which we will do by nesting an if. Don't need to worry about time overlap, if you posted at 23:59 then at 00:00 the comment was a day ago.
        // EG todayMonth is 07 and updateMonth is 07, then monthDiff is 0
        } else {

            // if yearDiff is 0, monthDiff is 0, and dayDiff is more than 14, then it's been more than 2 weeks but less than 1 month since the last update
            // EG todayDate is 17/07/2023 and updateDate is 01/07/2023, then yearDiff is 0, monthDiff is 0, and dayDiff is 16
            if (dayDiff > 13) {

                // Using floor to round to the nearest multiple of a week.
                // EG 16 days ago would be rounded down to 2 weeks ago
                durationAgo = Math.floor(dayDiff / 7) + timeIncrements[6];

            // if yearDiff is 0, monthDiff is 0, and dayDiff is more than 7, then it's been 1 week since the last update
            // EG todayDate is 15/07/2023 and updateDate is 07/07/2023, then yearDiff is 0, monthDiff is 0, and dayDiff is 8
            } else if (dayDiff > 6) {

                // Using floor to round to the nearest multiple of a week.
                // EG 8 days ago would be rounded down to 1 week ago 
                durationAgo = Math.floor(dayDiff / 7) + timeIncrements[5];
            
            // if yearDiff is 0, monthDiff is 0, and dayDiff is more than 1, then it's been a few days but less than a week since the last update
            // EG todayDate is 05/07/2023 and updateDate is 02/07/2023, then yearDiff is 0, monthDiff is 0, and dayDiff is 3
            } else if (dayDiff > 1) {
                durationAgo = dayDiff + timeIncrements[4];
            
            // if yearDiff is 0, monthDiff is 0, and dayDiff is exactly 1, then it's been 1 day since the last update
            // EG todayDate is 05/07/2023 and updateDate is 04/07/2023, then yearDiff is 0, monthDiff is 0, and dayDiff is 1
            } else if (dayDiff == 1) {
                durationAgo = dayDiff + timeIncrements[3];

            // if yearDiff is 0, monthDiff is 0, and dayDiff is 0, then it's been less than 24 hours since the last update
            // EG todayDate is 05/07/2023 and updateDate is 05/07/2023, then yearDiff is 0, monthDiff is 0, and dayDiff is 0
            } else {

                // If yearDiff is 0, monthDiff is 0, dayDiff is 0, and hourDiff is more than 1, then it's been more than 1 hour but less than 24 hours since the last update
                // EG todayDate is 17:30 05/07/2023 and updateDate is 10:20 05/07/2023, then hourDiff is 7
                if (hourDiff > 1) {
                    durationAgo = hourDiff + timeIncrements[2];

                // if yearDiff is 0, monthDiff is 0, dayDiff is 0, and hourDiff is 1, then it's been more than 1 hour but less than 2 hours since the last update
                // EG todayDate is 17:30 05/07/2023 and updateDate is 16:30 05/07/2023, then hourDiff is 1
                } else if (hourDiff == 1) {
                    durationAgo = hourDiff + timeIncrements[1];

                // if yearDiff is 0, monthDiff is 0, dayDiff is 0, and hourDiff is 0, then it's been less than 1 hour since the last update
                // EG todayDate is 17:30 05/07/2023 and updateDate is 17:15 05/07/2023, then hourDiff is 0.5, so it's been less than an hour but more than an hour
                } else if (hourDiff == 0) {
                    durationAgo = timeIncrements[0];
                
                // The only way this should be possible is if the update was made in the same hour as the page was loaded
                // EG todayDate is 17:00 05/07/2023 and updateDate is 17:00 05/07/2023, then hourDiff is 0
                } else {
                    durationAgo = "Time has begun to bend in on itself.";
                }
            }
        }
    };

    document.getElementById("last-active").innerHTML = durationAgo;

});
















// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// Flashbox Slideshow
// Create a slideshow of videos for the flashbox

// Create param
var videoIndex;

// Function to change to the next or previous video by pressing the left or right chevrons
function nextVideo(n) {
    showVideo(videoIndex += n);
}

// Function to change to the any video by pressing the preview images
function selectVideo(n) {
    showVideo(videoIndex = n);
}

// Function to determine which video to show
function showVideo(n) {

    // just for the for loop
    var i;
    
    // Get all the videos as an array based on class name "myVideos"
    var videos = document.getElementsByClassName("myVideos");

    // Get all the thumbnails as an array based on class name "thumbnail"
    var thumbnails = document.getElementsByClassName("thumbnail");

    // if n is greater than the number of slides, then reset n back to 1 (or to the start of the carousel)
    if (n > videos.length) {
        videoIndex = 1
    };

    // if n is less than 1, then reset n back to the last slide (or to the end of the carousel)
    if (n < 1) {
        videoIndex = videos.length
    };

    // Hide all the videos
    for (i = 0; i < videos.length; i++) {
        videos[i].style.display = "none";
    };

    // Remove the active class from all the thumbnails
    for (i = 0; i < thumbnails.length; i++) {
        thumbnails[i].className = thumbnails[i].className.replace(" active", "");
    };

    // Use the index to determine which video to show and give it display block
    videos[videoIndex - 1].style.display = "block";

    // Use the index to determine which thumbnail to give the active class to
    thumbnails[videoIndex - 1].className += " active";

    // testing 
    console.log("video index", videoIndex);
}






// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// 3D render Slideshow
// Create a slideshow of the 3D renders for the widget

// Always start on render #1 by default
var renderIndex = 1;

// Function to change to the next or previous render by pressing the left or right chevrons
function nextRender(n) {
    showRender(renderIndex += n);
}

// Function to change to the any render by pressing the dot
function selectRender(n) {
    showRender(renderIndex = n);
}

// Function to determine which render to show
function showRender(n) {

    // just for the for loop
    var j;
    
    // Get all the 3D renders as an array based on class name "myRenders"
    var renders = document.getElementsByClassName("myRenders");

    // Get all the dots as an array based on class name "dot"
    var dots = document.getElementsByClassName("dot");

    // if n is greater than the number of slides, then reset n back to 1 (or to the start of the carousel)
    if (n > renders.length) {
        renderIndex = 1
    }

    // if n is less than 1, then reset n back to the last slide (or to the end of the carousel)
    if (n < 1) {
        renderIndex = renders.length
    }

    // Hide all the 3D renders by default
    for (j = 0; j < renders.length; j++) {
        renders[j].style.display = "none";
    }

    // Remove the active class from all the dots
    for (j = 0; j < dots.length; j++) {
        dots[j].className = dots[j].className.replace(" active", "");
    }

    // Use the index to determine which 3D render to show and give it display block
    // // // // // // // // // // NOT DEFINED ON CONTENT LOADED BUT IS DEFINED WHEN BUTTON IS FIRST PUSHED
    renders[renderIndex - 1].style.display = "block";

    // Use the index to determine which dot to give the active class to
    dots[renderIndex - 1].className += " active";

    // testing 
    console.log("render index", renderIndex);
}