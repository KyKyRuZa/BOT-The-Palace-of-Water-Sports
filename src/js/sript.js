function changeClass() {
    document.getElementById('screen').classList.add('screen-inactive');
    document.getElementById('cnt').classList.add('screen-inactive');
    document.getElementById('logo').classList.add('screen-inactive');
    document.getElementById("cont").style.display = "block";
    document.getElementById("cont").classList.add('cont');
    document.getElementById("nav-inactive").classList.add('nav-active');
    document.getElementById("nav-inactive").style.opacity = 1;
}
