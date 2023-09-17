(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      return document.querySelector(el);
    }
  };

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach((e) => e.addEventListener(type, listener));
    } else {
      select(el, all).addEventListener(type, listener);
    }
  };

  /**
   * Easy on scroll event listener
   */
  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select("#navbar .scrollto", true);
  const navbarlinksActive = () => {
    let position = window.scrollY + 200;
    navbarlinks.forEach((navbarlink) => {
      if (!navbarlink.hash) return;
      let section = select(navbarlink.hash);
      if (!section) return;
      if (
        position >= section.offsetTop &&
        position <= section.offsetTop + section.offsetHeight
      ) {
        navbarlink.classList.add("active");
      } else {
        navbarlink.classList.remove("active");
      }
    });
  };
  window.addEventListener("load", navbarlinksActive);
  onscroll(document, navbarlinksActive);

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select("#header");
    let offset = header.offsetHeight;

    if (!header.classList.contains("header-scrolled")) {
      offset -= 10;
    }

    let elementPos = select(el).offsetTop;
    window.scrollTo({
      top: elementPos - offset,
      behavior: "smooth",
    });
  };

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select("#header");
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add("header-scrolled");
      } else {
        selectHeader.classList.remove("header-scrolled");
      }
    };
    window.addEventListener("load", headerScrolled);
    onscroll(document, headerScrolled);
  }

  /**
   * Back to top button
   */
  let backtotop = select(".back-to-top");
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add("active");
      } else {
        backtotop.classList.remove("active");
      }
    };
    window.addEventListener("load", toggleBacktotop);
    onscroll(document, toggleBacktotop);
  }

  /**
   * Mobile nav toggle
   */
  on("click", ".mobile-nav-toggle", function (e) {
    select("#navbar").classList.toggle("navbar-mobile");
    this.classList.toggle("bi-list");
    this.classList.toggle("bi-x");
  });

  /**
   * Mobile nav dropdowns activate
   */
  on(
    "click",
    ".navbar .dropdown > a",
    function (e) {
      if (select("#navbar").classList.contains("navbar-mobile")) {
        e.preventDefault();
        this.nextElementSibling.classList.toggle("dropdown-active");
      }
    },
    true
  );

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on(
    "click",
    ".scrollto",
    function (e) {
      if (select(this.hash)) {
        e.preventDefault();

        let navbar = select("#navbar");
        if (navbar.classList.contains("navbar-mobile")) {
          navbar.classList.remove("navbar-mobile");
          let navbarToggle = select(".mobile-nav-toggle");
          navbarToggle.classList.toggle("bi-list");
          navbarToggle.classList.toggle("bi-x");
        }
        scrollto(this.hash);
      }
    },
    true
  );

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener("load", () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash);
      }
    }
  });

  /**
   * Clients Slider
   */
  new Swiper(".clients-slider", {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40,
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 60,
      },
      640: {
        slidesPerView: 4,
        spaceBetween: 80,
      },
      992: {
        slidesPerView: 6,
        spaceBetween: 120,
      },
    },
  });

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener("load", () => {
    let portfolioContainer = select(".portfolio-container");
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: ".portfolio-item",
        layoutMode: "fitRows",
      });

      let portfolioFilters = select("#portfolio-flters li", true);

      on(
        "click",
        "#portfolio-flters li",
        function (e) {
          e.preventDefault();
          portfolioFilters.forEach(function (el) {
            el.classList.remove("filter-active");
          });
          this.classList.add("filter-active");

          portfolioIsotope.arrange({
            filter: this.getAttribute("data-filter"),
          });
          aos_init();
        },
        true
      );
    }
  });

  /**
   * Initiate portfolio lightbox
   */
  const portfolioLightbox = GLightbox({
    selector: ".portfokio-lightbox",
  });

  /**
   * Portfolio details slider
   */
  new Swiper(".portfolio-details-slider", {
    speed: 400,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
  });

  /**
   * Testimonials slider
   */
  new Swiper(".testimonials-slider", {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 40,
      },

      1200: {
        slidesPerView: 3,
      },
    },
  });

  /**
   * Animation on scroll
   */
  function aos_init() {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false,
    });
  }
  window.addEventListener("load", () => {
    aos_init();
  });
})();

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("deviceSelect")
    .addEventListener("change", function () {
      // Reset selections on device change
      document.getElementById("itemSelect").value = "";
      document.getElementById("subItemSelect").innerHTML = "";
      document.getElementById("currentSelectionContainer").innerHTML = "";
    });

  document.getElementById("itemSelect").addEventListener("change", function () {
    var itemValue = this.value;
    var subItemSelect = document.getElementById("subItemSelect");
    subItemSelect.innerHTML = "";

    if (itemValue) {
      if (itemValue === "Gaming") {
        addSubItem("LowEnd");
        addSubItem("HighEnd");
      } else if (itemValue === "Photography") {
        addSubItem("Low");
        addSubItem("Medium");
        addSubItem("High");
      } else if (itemValue === "Publishing") {
        addSubItem("Good");
        addSubItem("Better");
        addSubItem("Excellent");
      } else {
        addSubItem("Average");
        addSubItem("Optimal");
        addSubItem("Excellent");
      }
    }

    function addSubItem(subItemValue) {
      var option = document.createElement("option");
      option.value = subItemValue;
      option.textContent = subItemValue;
      subItemSelect.appendChild(option);
    }
  });
});

function addSelection() {
  var currentSelectionContainer = document.getElementById(
    "currentSelectionContainer"
  );
  var item = document.getElementById("itemSelect").value;
  var subItem = document.getElementById("subItemSelect").value;

  if (item && subItem) {
    var selectionText = item + " " + subItem;

    // Check if the parent item is already in the current selection
    var existingSelections =
      currentSelectionContainer.querySelectorAll(".selection-item");
    var parentItemAlreadySelected = false;

    existingSelections.forEach(function (selection) {
      if (selection.textContent.includes(item)) {
        parentItemAlreadySelected = true;
      }
    });

    if (!parentItemAlreadySelected) {
      var selectionElement = document.createElement("div");
      selectionElement.className = "selection-item";
      selectionElement.textContent = selectionText;

      var removeButton = document.createElement("span");
      removeButton.className = "remove-button";
      removeButton.textContent = "x";
      removeButton.addEventListener("click", function () {
        removeSelection(selectionElement);
      });

      selectionElement.appendChild(removeButton);
      currentSelectionContainer.appendChild(selectionElement);
    }

    // Reset selections
    document.getElementById("itemSelect").value = "";
    document.getElementById("subItemSelect").innerHTML = "";
  }
}

function removeSelection(selection) {
  var currentSelectionContainer = document.getElementById(
    "currentSelectionContainer"
  );
  currentSelectionContainer.removeChild(selection);
}

function search() {
  var currentSelectionContainer = document.getElementById(
    "currentSelectionContainer"
  );
  var selections =
    currentSelectionContainer.querySelectorAll(".selection-item");

  // Initialize an empty dictionary
  var searchDict = {};

  selections.forEach(function (selection) {
    var selectionText = selection.textContent;
    var parts = selectionText.split(" ");

    if (parts.length === 2) {
      var item = parts[0];
      var subItem = parts[1];

      // remove the x button for delete
      var subItem = parts[1].replace("x", "");

      // Add to the dictionary
      searchDict[item] = subItem;
    }
  });

  // Send the searchDict to your backend
  sendToBackend(searchDict);
}

function sendToBackend(searchDict) {
  // Send a POST request to your Python backend
  fetch("/search", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(searchDict),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Handle the response from the backend
      console.log(data);
      var queryString = data.map((obj) => `model_id=${obj.model_id}`).join("&");
      window.location.href = `/result?${queryString}`;
  })
  .catch(error => {
      console.error('Error:', error);
  });
  console.log('Data to be sent to backend:', searchDict);
}

// slider

var mySwiper = new Swiper(".swiper-container", {
  direction: "vertical",
  loop: true,
  pagination: ".swiper-pagination",
  grabCursor: true,
  speed: 1000,
  paginationClickable: true,
  parallax: true,
  autoplay: true,
  effect: "slide",
  mousewheelControl: 1
});
