const apiKey = "601eb41b5288828ff7460828";
const apiUrl = `https://v6.exchangerate-api.com/v6/${apiKey}/latest/USD`;

const fromCurrencySelect = document.getElementById("fromCurrency");
const toCurrencySelect = document.getElementById("toCurrency");
const amountInput = document.getElementById("amount");
const convertButton = document.getElementById("convertButton");
const resultContainer = document.getElementById("resultContainer");

let exchangeRates = {};

// Fetch all supported currencies and populate dropdowns
async function fetchCurrencies() {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();

    if (data.result === "success") {
      exchangeRates = data.conversion_rates;
      const currencies = Object.keys(exchangeRates);
      populateCurrencyOptions(currencies);
    } else {
      console.error("Error fetching currencies:", data.message);
    }
  } catch (error) {
    console.error("Error fetching currencies:", error);
  }
}

// Populate currency options in select dropdowns
function populateCurrencyOptions(currencies) {
  currencies.forEach((currency) => {
    const option1 = new Option(currency, currency);
    const option2 = new Option(currency, currency);
    fromCurrencySelect.appendChild(option1);
    toCurrencySelect.appendChild(option2);
  });
}

// Convert currency
function convertCurrency() {
  const fromCurrency = fromCurrencySelect.value;
  const toCurrency = toCurrencySelect.value;
  const amount = parseFloat(amountInput.value);

  if (isNaN(amount)) {
    resultContainer.textContent = "Please enter a valid amount.";
    return;
  }

  if (fromCurrency === toCurrency) {
    resultContainer.textContent = "Please select different currencies.";
    return;
  }

  if (!exchangeRates[fromCurrency] || !exchangeRates[toCurrency]) {
    resultContainer.textContent = "Exchange rates not available.";
    return;
  }

  const exchangeRate = exchangeRates[toCurrency] / exchangeRates[fromCurrency];
  const convertedAmount = (amount * exchangeRate).toFixed(2);
  resultContainer.textContent = `${amount} ${fromCurrency} = ${convertedAmount} ${toCurrency}`;
}

// Event listeners
convertButton.addEventListener("click", convertCurrency);

// Fetch all supported currencies on page load
fetchCurrencies();
