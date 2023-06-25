document.getElementById("libform").addEventListener("submit", function(event) {
    event.preventDefault();

    var noun = document.getElementById("noun").value.trim();
    var adjective = document.getElementById("adjective").value.trim();
    var person = document.getElementById("person").value.trim();
    var verb = document.getElementById("verb").value.trim();
    var place = document.getElementById("place").value.trim();

    if (noun === "" || adjective === "" || person === "" || verb === "" || place === "") {
        console.error("Please enter all the values.");
        return;
    }

    var story = generateStory(noun, adjective, person, verb, place);
    document.getElementById("story").textContent = story;
});

function generateStory(noun, adjective, person, verb, place) {
    var story = "Once upon a time, there was a " + adjective + " " + noun + ". ";
    story += person + " " + verb + " to the " + place + ".";
    return story;
}

document.getElementById("shuffle-button").addEventListener("click", function() {
    var noun = document.getElementById("noun").value.trim();
    var adjective = document.getElementById("adjective").value.trim();
    var person = document.getElementById("person").value.trim();
    var verb = document.getElementById("verb").value.trim();
    var place = document.getElementById("place").value.trim();

    var stories = [
        generateStory(noun, adjective, person, verb, place),
        generateStory(adjective, verb, noun, place, person),
        generateStory(person, place, adjective, verb, noun)
    ];

    var randomStory = stories[Math.floor(Math.random() * stories.length)];
    document.getElementById("story").textContent = randomStory;
});
