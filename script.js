document.getElementById("calculateButton").addEventListener("click", function () {
    const loanAmount = parseFloat(document.getElementById("loanAmount").value);
    const loanTerm = parseInt(document.getElementById("loanTerm").value);
    const monthlyInterestRate = parseFloat(document.getElementById("monthlyInterestRate").value);


    const monthlyInterestRateDecimal = monthlyInterestRate / 100;
    const monthlyPayment = (loanAmount * monthlyInterestRateDecimal) * ((1 + monthlyInterestRateDecimal) ** (loanTerm)) / (((1 + monthlyInterestRateDecimal) ** (loanTerm))-1);
    const totalCost = monthlyPayment * loanTerm;
    const annualInterestRate = (((1 + (monthlyInterestRate/100)) ** (12) -1) * 100);
    document.getElementById("annualInterestRate").textContent = "Annual Interest Rate: " + annualInterestRate.toFixed(2) + "%";
    document.getElementById("monthlyPayment").textContent = "Monthly Payment: $" + monthlyPayment.toFixed(2);
    document.getElementById("totalCost").textContent = "Total Cost: $" + totalCost.toFixed(2);
    
})