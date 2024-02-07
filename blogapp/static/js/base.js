document.addEventListener("DOMContentLoaded", function(){
    navbar_height = document.querySelector('.navbar').offsetHeight;
    document.body.style.paddingTop = navbar_height + 'px';
  }); 