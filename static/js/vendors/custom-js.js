// custom-slider.js
document.addEventListener("DOMContentLoaded", function () {
    var modalSlider, productSlider;

    if (document.querySelectorAll(".productModal").length > 0) {
        modalSlider = tns({
            container: "#productModal",
            items: 1,
            startIndex: 0,
            navContainer: "#productModalThumbnails",
            navAsThumbnails: true,
            autoplay: false,
            autoplayTimeout: 1500,
            swipeAngle: false,
            speed: 1500,
            controls: false,
            autoplayButtonOutput: false,
            loop: false
        });
    }

    if (document.querySelectorAll(".product").length > 1) {
        productSlider = tns({
            container: "#product",
            items: 1,
            startIndex: 0,
            navContainer: "#productThumbnails",
            navAsThumbnails: true,
            autoplay: false,
            autoplayTimeout: 1500,
            swipeAngle: false,
            speed: 1500,
            controls: false,
            autoplayButtonOutput: false
        });
    }
});
