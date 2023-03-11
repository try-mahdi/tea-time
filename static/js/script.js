function sendOrder() {
    var btn = document.getElementById("order-btn");
    var input1 = document.getElementById("input1");
    var input2 = document.getElementById("input2");
    
    if (input1.value === "" || input2.value === "") {
      alert("Please fill in both boxes.");
      return;
    }
    
    btn.classList.add("order-sent");
    btn.innerHTML = '<i class="fas fa-check"></i> Order Sent';
  }
  