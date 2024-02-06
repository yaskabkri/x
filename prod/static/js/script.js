
document.getElementById("menu-button").addEventListener("click", function() {
    document.getElementById("sidebar").classList.toggle("sidebar-visible");
});

function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");

    if (sidebar.style.width === "250px") {
        sidebar.style.width = "0";
    } else {
        sidebar.style.width = "250px";
    }
}
