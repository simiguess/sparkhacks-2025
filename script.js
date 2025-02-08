const companies = [
    {
        name: "The Restaurant",
        description: "Local faminly owned busniess, been here for 7 generations ",
        rating: "4/5",
        employees: "6",
        image: "images/restaurant.png"
    },
    {
        name: "The Flower Company",
        description: "a new business just budding  ",
        rating: "5/5",
        employees: "3",
        image: "images/flower.png"
    },
    {
        name: "Salon",
        description: "Come is and get a fresh cut with your freindky neighborhood barber ",
        rating: "4/5",
        employees: "7",
        image: "images/salon.png"
    },
    {
        name: "Coffee cup ",
        description: "O'l cup of joeContrary to popular trary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 ofbelief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more trary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 ofobscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of ",
        rating: "4.5/5",
        employees: "12",
        image: "images/coffee-cup.png"
    },
    {
        name: "Books galore ",
        description: "come expam your mind ",
        rating: "3/5",
        employees: "6",
        image: "images/books-piled-.png"
    }
];

const companyContainer = document.getElementById("companies");

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
    `;

    companyContainer.appendChild(companyBox);
});
