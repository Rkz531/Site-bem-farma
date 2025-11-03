// Scroll suave
function scrollToSection(id){
    document.getElementById(id).scrollIntoView({behavior:"smooth"});
}

// Download
function baixarApp(sistema){
    if(sistema==="android"){
        window.location.href="https://play.google.com/store";
    } else if(sistema==="ios"){
        window.location.href="https://www.apple.com/br/app-store/";
    }
}

// Carrossel
let slideIndex = 0;
const slides = document.querySelectorAll('.carrossel-img');

function mostrarSlide(index){
    slides.forEach((slide, i) => slide.style.transform = `translateX(-${index*100}%)`);
}
function mudarSlide(n){
    slideIndex += n;
    if(slideIndex < 0) slideIndex = slides.length-1;
    if(slideIndex >= slides.length) slideIndex = 0;
    mostrarSlide(slideIndex);
}
mostrarSlide(slideIndex);

// Alto contraste
function ativarAltoContraste(){
    document.body.classList.toggle('contraste');
}
