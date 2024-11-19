import streamlit as st
import streamlit.components.v1 as components

# Save your HTML content as a string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Alphabet Cards</title>
  <style>
    body {
      margin: 0;
      background-color: #f0f0f0;
      padding: 1rem;
      font-family: Arial, sans-serif;
    }

    .vowels-container {
      display: flex;
      justify-content: center;
      gap: 0.5rem;
      margin: 1rem 0;
    }

    .divider {
      height: 5px;
      background-color: white;
      margin: 1rem 0;
    }

    .consonants-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1rem;
    }

    .consonants-row {
      display: flex;
      gap: 0.5rem;
    }

    .card {
      width: 100px;
      height: 60px;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      font-size: 1.5rem;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="vowels-container" id="vowels-container"></div>
  <div class="divider"></div>
  <div class="consonants-container" id="consonants-container"></div>

  <script>
    // Define vowels and consonants
    const vowels = ['A', 'E', 'I', 'O', 'U'];
    const consonants = [
      ['B', 'C', 'D'], // Row 1: 3 cards
      ['F', 'G', 'H', 'J', 'K'], // Row 2: 5 cards
      ['L', 'M', 'N', 'P', 'Q'], // Row 3: 5 cards
      ['R', 'S', 'T', 'V', 'W'], // Row 4: 5 cards
      ['X', 'Y'] // Row 5: 2 cards
    ];

    // Generate a unique color for each card
    function getRandomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }

    // Function to create cards
    function createCards(letters, rowContainer) {
      letters.forEach((letter) => {
        const card = document.createElement('div');
        card.classList.add('card');
        const color = getRandomColor();
        card.style.backgroundColor = color;
        card.style.color = color; // Match letter color to card background
        card.textContent = letter;
        rowContainer.appendChild(card);
      });
    }

    // Populate vowels
    const vowelsContainer = document.getElementById('vowels-container');
    createCards(vowels, vowelsContainer);

    // Populate consonants
    const consonantsContainer = document.getElementById('consonants-container');
    consonants.forEach((row) => {
      const rowContainer = document.createElement('div');
      rowContainer.classList.add('consonants-row');
      createCards(row, rowContainer);
      consonantsContainer.appendChild(rowContainer);
    });
  </script>
</body>
</html>
"""

# Embed the HTML in the Streamlit app
st.title("The Silent Way")
components.html(html_content, height=600, scrolling=True)
