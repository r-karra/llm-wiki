document.addEventListener("DOMContentLoaded", function() {
  
  // 1. Mobile Sidebar Toggle
  const sidebarToggle = document.getElementById("sidebar-toggle");
  const sidebar = document.getElementById("sidebar");

  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener("click", function(e) {
      sidebar.classList.toggle("open");
      e.stopPropagation();
    });

    // Close sidebar when clicking outside on mobile
    document.addEventListener("click", function(e) {
      if (window.innerWidth <= 768 && sidebar.classList.contains("open")) {
        if (!sidebar.contains(e.target) && e.target !== sidebarToggle) {
          sidebar.classList.remove("open");
        }
      }
    });
  }

  // 2. Client-side Wiki Search
  const searchInput = document.getElementById("wiki-search");
  if (searchInput) {
    searchInput.addEventListener("input", function(e) {
      const query = e.target.value.toLowerCase().trim();
      const navSections = document.querySelectorAll(".sidebar-nav .nav-section");

      navSections.forEach(section => {
        let visibleCount = 0;
        const items = section.querySelectorAll(".nav-item");
        const title = section.querySelector(".nav-section-title");

        items.forEach(item => {
          // If the item is the main Home item and query is active, let's keep it visible
          const text = item.innerText.toLowerCase();
          const isHome = item.getAttribute("href") === "/" || item.getAttribute("href") === "/index.html";

          if (query === "") {
            item.style.display = "flex";
            visibleCount++;
          } else {
            if (text.includes(query) && !isHome) {
              item.style.display = "flex";
              visibleCount++;
            } else if (isHome) {
              item.style.display = "none";
            } else {
              item.style.display = "none";
            }
          }
        });

        // Hide section title if all items inside are hidden
        if (title) {
          if (visibleCount === 0 && query !== "") {
            title.style.display = "none";
          } else {
            title.style.display = "block";
          }
        }
      });
    });
  }

  // 3. Add Copy Buttons to Code Blocks
  const codeBlocks = document.querySelectorAll("pre");
  codeBlocks.forEach(pre => {
    // Check if the pre already has a copy button (prevent duplicate run)
    if (pre.querySelector(".code-header")) return;

    // Create header container for copy button
    const headerDiv = document.createElement("div");
    headerDiv.className = "code-header";

    const button = document.createElement("button");
    button.className = "copy-btn";
    button.type = "button";
    button.innerHTML = `
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
      <span>Copy</span>
    `;

    button.addEventListener("click", function() {
      const code = pre.querySelector("code");
      if (!code) return;

      const text = code.innerText;
      navigator.clipboard.writeText(text).then(() => {
        button.querySelector("span").innerText = "Copied!";
        button.style.borderColor = "#10b981";
        button.style.color = "#10b981";
        
        setTimeout(() => {
          button.querySelector("span").innerText = "Copy";
          button.style.borderColor = "";
          button.style.color = "";
        }, 2000);
      }).catch(err => {
        console.error("Could not copy text: ", err);
      });
    });

    headerDiv.appendChild(button);
    pre.insertBefore(headerDiv, pre.firstChild);
  });
});
