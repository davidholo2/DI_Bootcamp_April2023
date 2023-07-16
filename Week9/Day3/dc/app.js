const apiKey = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const apiUrl = "https://api.giphy.com/v1/gifs/random";

const searchForm = document.getElementById("searchForm");
const searchInput = document.getElementById("searchInput");
const gifContainer = document.getElementById("gifContainer");
const deleteAllButton = document.getElementById("deleteAllButton");

searchForm.addEventListener("submit", fetchAndDisplayGif);

function fetchAndDisplayGif(event) {
  event.preventDefault();
  const searchTerm = searchInput.value.trim();
  if (!searchTerm) return;

  const fetchUrl = `${apiUrl}?tag=${searchTerm}&api_key=${apiKey}`;

  fetch(fetchUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      const gifUrl = data.data.images.original.url;
      appendGifToContainer(gifUrl, searchTerm);
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}

function appendGifToContainer(gifUrl, searchTerm) {
  const gifElement = document.createElement("div");
  gifElement.classList.add("gif");
  gifElement.innerHTML = `
    <img src="${gifUrl}" alt="${searchTerm}">
    <button class="deleteButton">DELETE</button>
  `;

  gifContainer.appendChild(gifElement);

  const deleteButton = gifElement.querySelector(".deleteButton");
  deleteButton.addEventListener("click", () => {
    gifContainer.removeChild(gifElement);
  });
}

deleteAllButton.addEventListener("click", () => {
  gifContainer.innerHTML = "";
});
