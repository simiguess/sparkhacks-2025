async function loadPrizes() {
    try {
        const response = await fetch("/prizes.json");
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const prizeData = await response.json();
        console.log("Loaded prize data:", prizeData); // Debugging step

        const rarityIcons = {
            "common": "/static/images/common.png",
            "uncommon": "/static/images/uncommon.png",
            "rare": "/static/images/rare.png",
            "epic": "/static/images/epic.png",
            "legendary": "/static/images/legendary.png"
        };

        document.querySelectorAll(".company-box").forEach(companyBox => {
            const companyName = companyBox.querySelector("h2").textContent.trim();
            
            if (prizeData[companyName]) {
                let iconContainer = document.createElement("div");
                iconContainer.classList.add("icon-container");

                // Add multiple icons for multiple prizes
                prizeData[companyName].prizes.forEach(prize => {
                    let prizeIcon = rarityIcons[prize.rarity] || "https://cdn-icons-png.flaticon.com/128/190/190411.png";
                    let icon = document.createElement("img");
                    icon.src = prizeIcon;
                    icon.alt = prize.rarity;
                    icon.classList.add("icon");
                    iconContainer.appendChild(icon);
                });

                // Append icons BELOW the company info section
                companyBox.appendChild(iconContainer);
            } else {
                console.warn(`No prize found for: ${companyName}`);
            }
        });

    } catch (error) {
        console.error("Error loading prizes:", error);
    }
}

const companyContainer = document.getElementById("companies");

const companies = [
    {
        name: "The Restaurant",
        description: "Local family-owned business, serving for 7 generations. Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        rating: "4/5",
        employees: "6",
        image: "/static/images/restaurant.png"
    },
    {
        name: "The Flower Company",
        description: "A new business just budding. Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        rating: "5/5",
        employees: "3",
        image: "/static/images/flower.png"
    },
    {
        name: "Salon",
        description: "Come in and get a fresh cut with your friendly neighborhood barber. Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        rating: "4/5",
        employees: "7",
        image: "/static/images/salon.png"
    },
    {
        name: "Coffee Cup",
        description: "A classic cup of joe! A cozy place with a rich history. Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        rating: "4.5/5",
        employees: "12",
        image: "/static/images/coffee-cup.png"
    },
    {
        name: "Books Galore",
        description: "Come expand your mind with our vast collection. Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        rating: "3/5",
        employees: "6",
        image: "/static/images/books-piled-.png"
    } 
];

// Populate company cards
companies.forEach(company => {
    const companyBox = document.createElement("div");
    companyBox.classList.add("company-box");

    companyBox.innerHTML = `
        <img src="${company.image}" alt="${company.name}" class="company-image">
        <div class="company-info">
            <h2>${company.name}</h2>
            <p><strong>Description:</strong> ${company.description}</p>
            <p><strong>Rating:</strong> ${company.rating}</p>
            <p><strong>Employees:</strong> ${company.employees}</p>
        </div>
        <!-- ICONS WILL BE ADDED BELOW THIS WITH JAVASCRIPT -->
    `;

    companyContainer.appendChild(companyBox);
});

// Load prizes when the script runs
loadPrizes();
