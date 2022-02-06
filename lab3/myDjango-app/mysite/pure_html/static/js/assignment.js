let showTeam = document.getElementById("show-team-btn")
let myName = document.getElementById("show-name")

showTeam.addEventListener("click", () => {
    console.log("here");
    all_teamMates = ""
    for (let d = 0; d < teammates.length; d++) {
        all_teamMates += "<li>" + teammates[d] + "</li>";
    }
    console.log(all_teamMates);
    myName.innerHTML = all_teamMates;
})