// var stripe = Stripe(stripePublishableKey);
// var checkoutButton = document.getElementById("checkout-button");

// checkoutButton.addEventListener("click", function () {
//     console.log("Button clicked");

//     var email = document.getElementById("myemail").innerText.trim();

//     if (!email) {
//       alert("Please enter your email address");
//       return;
//     }

// fetch(checkoutSessionUrl, {
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json",
//     "X-CSRFToken": "{{ csrf_token }}"
//   },
//   body: JSON.stringify({ email: email })
// })
//       .then(response => response.json())
//       .then(session => stripe.redirectToCheckout({ sessionId: session.sessionId }))
//       .catch(error => console.error("Error:", error));
// });
