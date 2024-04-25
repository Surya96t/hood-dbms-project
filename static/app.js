let items = document.querySelectorAll('.slider .list .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let thumbnails = document.querySelectorAll('.thumbnail .item');

// config param
let countItem = items.length;
let itemActive = 0;
// event next click
next.onclick = function(){
    itemActive = itemActive + 1;
    if(itemActive >= countItem){
        itemActive = 0;
    }
    showSlider();
}
//event prev click
prev.onclick = function(){
    itemActive = itemActive - 1;
    if(itemActive < 0){
        itemActive = countItem - 1;
    }
    showSlider();
}
// auto run slider
let refreshInterval = setInterval(() => {
    next.click();
}, 5000)
function showSlider(){
    // remove item active old
    let itemActiveOld = document.querySelector('.slider .list .item.active');
    let thumbnailActiveOld = document.querySelector('.thumbnail .item.active');
    itemActiveOld.classList.remove('active');
    thumbnailActiveOld.classList.remove('active');

    // active new item
    items[itemActive].classList.add('active');
    thumbnails[itemActive].classList.add('active');

    // clear auto time run slider
    clearInterval(refreshInterval);
    refreshInterval = setInterval(() => {
        next.click();
    }, 5000)
}

// click thumbnail
thumbnails.forEach((thumbnail, index) => {
    thumbnail.addEventListener('click', () => {
        itemActive = index;
        showSlider();
    })
})


var aa = 0;
function increaseA(){
    aa += 20000;
    document.getElementById('one').value = aa;
    document.getElementById('aa').value = aa/20000;
    bill();
}
function decreaseA(){
    if(aa > 0){
        aa -= 20000;
        document.getElementById('one').value = aa;
        document.getElementById('aa').value = aa/20000;
    bill();
    }
}
var bb = 0;
function increaseB(){
    bb += 30000;
    document.getElementById('two').value = bb;
    document.getElementById('bb').value = bb/30000;
    bill();
}
function decreaseB(){
    if(bb > 0){
        bb -= 30000;
        document.getElementById('two').value = bb;
        document.getElementById('bb').value = bb/30000;
    bill();
    }
}
var cc = 0;
function increaseC(){
    cc += 40000;
    document.getElementById('three').value = cc;
    document.getElementById('cc').value = cc/40000;
    bill();
}
function decreaseC(){
    if(cc > 0){
        cc -= 40000;
        document.getElementById('three').value = cc;
        document.getElementById('cc').value = cc/40000;
    bill();
    }
}
var dd = 0;
function increaseD(){
    dd += 30000;
    document.getElementById('four').value = dd;
    document.getElementById('dd').value = dd/30000;
    bill();
}
function decreaseD(){
    if(dd > 0){
        dd -= 30000;
        document.getElementById('four').value = dd;
        document.getElementById('dd').value = dd/30000;
    bill();
    }
}
var ee = 0;
function increaseE(){
    ee += 20000;
    document.getElementById('five').value = ee;
    document.getElementById('ee').value = ee/20000;
    bill();
}
function decreaseE(){
    if(ee > 0){
        ee -= 20000;
        document.getElementById('five').value = ee;
        document.getElementById('ee').value = ee/20000;
    bill();
    }
}
function bill() {
    total1= aa + bb + cc + dd + ee;
    document.getElementById("total").innerHTML = total1;
}
function list() {
    if(aa>0)
    document.getElementById("MAC").innerHTML = "MACARONI AND CHEESE ("+aa/20000 + ")";
    if(bb>0)
    document.getElementById("LAS").innerHTML = "CHEESE LASAGNA ("+bb/30000 + ")";
    if(cc>0)
    document.getElementById("OME").innerHTML = "MOZZARELLA CHEESE OMELETTE ("+cc/40000 + ")";
    if(dd>0)
    document.getElementById("OCH").innerHTML = "OREO CHEESECAKE ("+dd/30000 + ")";
    if(ee>0)
    document.getElementById("OMI").innerHTML = "OREO MILKSHAKE ("+ee/20000 + ")";
    document.getElementById("lister").innerHTML = total1;
    emp();
}
function emp() {
aa = 0;
document.getElementById('one').value = 0;
document.getElementById('aa').value = 0;
bb = 0;
document.getElementById('two').value = 0;
document.getElementById('bb').value = 0;
cc = 0;
document.getElementById('three').value = 0;
document.getElementById('cc').value = 0;
dd = 0;
document.getElementById('four').value = 0;
document.getElementById('dd').value = 0;
ee = 0;
document.getElementById('five').value = 0;
document.getElementById('ee').value = 0;
}	
