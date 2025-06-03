// DOM elements
const nextDom = document.getElementById('next');
const prevDom = document.getElementById('prev');
const carouselDom = document.querySelector('.carousel');
const SliderDom = carouselDom.querySelector('.carousel .list');
const thumbnailBorderDom = document.querySelector('.carousel .thumbnail');
let thumbnailItemsDom = thumbnailBorderDom.querySelectorAll('.item');

// Inicial: mueve el primer thumbnail al final
thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);

// Tiempos
const timeRunning = 3000;
const timeAutoNext = 7000;

// Botones
nextDom.onclick = () => showSlider('next');
prevDom.onclick = () => showSlider('prev');

// Auto avance
let runTimeOut;
let runNextAuto = setTimeout(() => {
    nextDom.click();
}, timeAutoNext);

// Función principal de cambio
function showSlider(type) {
    const SliderItemsDom = SliderDom.querySelectorAll('.carousel .list .item');
    const thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');
    
    if (type === 'next') {
        SliderDom.appendChild(SliderItemsDom[0]);
        thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
        carouselDom.classList.add('next');
    } else {
        SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
        thumbnailBorderDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
        carouselDom.classList.add('prev');
    }

    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        carouselDom.classList.remove('next');
        carouselDom.classList.remove('prev');
    }, timeRunning);

    clearTimeout(runNextAuto);
    runNextAuto = setTimeout(() => {
        nextDom.click();
    }, timeAutoNext);
}
