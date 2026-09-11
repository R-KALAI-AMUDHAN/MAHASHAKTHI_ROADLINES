/* MAHASHAKTHI ROADLINES — shared site behaviour */
(function () {
  "use strict";

  var WHATSAPP_NUMBER = "919677079089"; // +91 9677079089, international format for wa.me
  var DEFAULT_WA_MESSAGE = "Hello MAHASHAKTHI ROADLINES, I would like to enquire about your transportation services.";

  function waLink(message) {
    var msg = message || DEFAULT_WA_MESSAGE;
    return "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(msg);
  }

  // Wire up every element with data-wa-link (optionally data-wa-message="...")
  function initWhatsAppLinks() {
    var nodes = document.querySelectorAll("[data-wa-link]");
    nodes.forEach(function (el) {
      el.setAttribute("href", waLink(el.getAttribute("data-wa-message")));
      el.setAttribute("target", "_blank");
      el.setAttribute("rel", "noopener");
    });
  }

  // Mobile nav toggle
  function initMobileNav() {
    var toggle = document.querySelector(".nav-toggle");
    var panel = document.querySelector(".mobile-nav");
    if (!toggle || !panel) return;
    toggle.addEventListener("click", function () {
      var isOpen = panel.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      document.body.style.overflow = isOpen ? "hidden" : "";
    });
    panel.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        panel.classList.remove("open");
        document.body.style.overflow = "";
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Number counters for the genuine stats strip
  function initCounters() {
    var counters = document.querySelectorAll("[data-count-to]");
    if (!counters.length) return;
    var run = function (el) {
      var target = parseInt(el.getAttribute("data-count-to"), 10);
      var suffix = el.getAttribute("data-count-suffix") || "";
      var duration = 900;
      var start = null;
      function step(ts) {
        if (start === null) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(eased * target) + suffix;
        if (progress < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    };
    if (!("IntersectionObserver" in window)) {
      counters.forEach(run);
      return;
    }
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            run(entry.target);
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach(function (el) { io.observe(el); });
  }

  // Quote form: frontend-only validation + success state.
  // No backend/email service is configured yet — this does not
  // send an email. It is structured so a real submission handler
  // (API call / email service) can be dropped into handleSubmit().
  function initQuoteForm() {
    var form = document.getElementById("quote-form");
    if (!form) return;
    var successEl = document.getElementById("quote-success");

    function setError(field, message) {
      var wrapper = field.closest(".field");
      if (!wrapper) return;
      wrapper.classList.add("has-error");
      var msgEl = wrapper.querySelector(".error-msg");
      if (msgEl) msgEl.textContent = message;
    }
    function clearError(field) {
      var wrapper = field.closest(".field");
      if (!wrapper) return;
      wrapper.classList.remove("has-error");
    }

    function isValidPhone(value) {
      var digits = value.replace(/\D/g, "");
      return digits.length >= 10;
    }
    function isValidEmail(value) {
      if (!value) return true; // email optional
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var valid = true;
      var requiredFields = form.querySelectorAll("[required]");
      requiredFields.forEach(function (field) {
        clearError(field);
        if (!field.value || !field.value.trim()) {
          setError(field, "This field is required.");
          valid = false;
        }
      });

      var phone = form.querySelector("#quote-phone");
      if (phone && phone.value && !isValidPhone(phone.value)) {
        setError(phone, "Enter a valid mobile number.");
        valid = false;
      }
      var email = form.querySelector("#quote-email");
      if (email && email.value && !isValidEmail(email.value)) {
        setError(email, "Enter a valid email address.");
        valid = false;
      }

      if (!valid) {
        var firstError = form.querySelector(".has-error input, .has-error select, .has-error textarea");
        if (firstError) firstError.focus();
        return;
      }

      // handleSubmit(new FormData(form)) — connect a backend/email API here.
      form.style.display = "none";
      if (successEl) successEl.classList.add("show");
    });

    form.querySelectorAll("input, select, textarea").forEach(function (field) {
      field.addEventListener("input", function () { clearError(field); });
      field.addEventListener("change", function () { clearError(field); });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initWhatsAppLinks();
    initMobileNav();
    initCounters();
    initQuoteForm();
  });
})();
