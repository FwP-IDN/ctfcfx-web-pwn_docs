function toggleList(elementId) {
    var list = document.getElementById("ul_" + elementId);
    var icon = document.getElementById("btn_" + elementId);

    if (list.style.display == "block"){
        list.style.display = "none";
    }
    else{
        list.style.display = "block";
    }

    if (icon.style.backgroundColor == "rgb(0, 127, 127)") {
        icon.style.backgroundColor = "#00007F";
        icon.style.color = "#00007F"
    }
    else {
        icon.style.backgroundColor = "#007F7F";
        icon.style.color = "#007F7F";
    }
}

function openNewTab(link) {
    window.open(link,'_blank');
}
