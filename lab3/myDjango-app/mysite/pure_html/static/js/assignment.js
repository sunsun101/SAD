let showTeam = document.getElementById("show-team-btn")
let myName = document.getElementById("show-name")

showTeam.addEventListener("click", () => {
    myName.innerHTML = teammates;
})