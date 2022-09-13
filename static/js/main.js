let navbar = document.querySelector("nav");
let video = document.querySelector(".video-player");
let userInfo = document.querySelector(".info");

let cart = {
  items: [],
  totalPrice: 0,
  totalQuantity: 0,
};
let amount = 1;

window.onscroll = () => {
  if (window.pageYOffset > 80) {
    navbar.classList.add("fixed");
  } else {
    navbar.classList.remove("fixed");
  }
};

window.onload = () => {
  const localStorageCart = JSON.parse(localStorage.getItem("cartItems"));
  if (localStorageCart) {
    cart = localStorageCart;
    setCartItems();
    whenCartisEmpty();
  }
};

const whenCartisEmpty = () => {
  if (cart.items.length === 0) {
    document.querySelector(".cart .whenEmpty").style.display = "block";
    document.querySelector(".cart .total").style.display = "none";
  } else {
    document.querySelector(".cart .whenEmpty").style.display = "none";
    document.querySelector(".cart .total").style.display = "block";
  }
};
whenCartisEmpty();

const toggleVideo = () => {
  video.classList.toggle("close");
};

const toggleUserInfo = () => {
  userInfo.classList.toggle("close");
};

const toggleCart = () => {
  const cart = document.querySelector(".cart");
  const cartOverlay = document.querySelector(".cart-overlay");
  cart.classList.toggle("showCart");
  cartOverlay.classList.toggle("show-cart-overlay");
};

const increaseProductAmount = () => {
  const amountInput = document.querySelector(".amountInput input");
  amount++;
  amountInput.setAttribute("value", amount);
};

const decreaseProductAmount = () => {
  const amountInput = document.querySelector(".amountInput input");
  if (amount != 0) {
    amount--;
    amountInput.setAttribute("value", amount);
  }
};

const addProductToCart = () => {
  if (amount != 0) {
    const totalPrice = +data.price * amount;
    let newItem = { ...data, amount: amount, totalPrice: totalPrice };
    const existingItem = cart.items.find((item) => item.id === data.id);

    if (!existingItem) {
      cart.items.push(newItem);
    } else {
      existingItem.amount += newItem.amount;
      existingItem.totalPrice += newItem.totalPrice;
    }
    cart.totalPrice += newItem.totalPrice;
    cart.totalQuantity += newItem.amount;
    localStorage.setItem("cartItems", JSON.stringify(cart));
    document.querySelector(
      ".cart .totalPrice"
    ).innerHTML = `$${cart.totalPrice}`;
    document.querySelector(".shoppingBag span").textContent =
      cart.totalQuantity;
    setCartItems();
  }
  whenCartisEmpty();
};

const removeItemFromCart = (id) => {
  const existingItem = cart.items.find((item) => item.id === id);
  if (existingItem.amount === 1) {
    cart.items = cart.items.filter((item) => item.id !== id);
  } else {
    existingItem.amount--;
    existingItem.totalPrice -= existingItem.price;
  }
  cart.totalQuantity--;
  cart.totalPrice -= existingItem.price;
  localStorage.setItem("cartItems", JSON.stringify(cart));
  document.querySelector(
    ".cart .totalPrice"
  ).textContent = `$${cart.totalPrice}`;
  document.querySelector(".shoppingBag span").textContent = cart.totalQuantity;
  setCartItems();
  whenCartisEmpty();
};

const setCartItems = () => {
  const cartItemsContainer = document.querySelector(".cart .cartItems");
  cartItemsContainer.innerHTML = "";
  document.querySelector(".shoppingBag span").textContent = cart.totalQuantity;
  cart.items.forEach((item) => {
    const xmlString = `
        <div class="cartItem">
        <div class="image">
          <img src="/media_imgs/${item.image1}"/>
        </div> 
        <div class="productInfo">
          <h5>${item.name}</h5>
          <p class="props"></p>
          <h5>$ ${item.totalPrice}.00</h5>
          <div class="amountInput">
            <p class="reduce" onclick="removeItemFromCart(${item.id})">
              -
            </p>
            <input
              type="number"
              name="amount"
              min="1"
              value="${item.amount}"
            />
            <p class="increase" onclick="addProductToCart()">
              +
            </p>
          </div>
        </div>
      </div>
    `;
    cartItemsContainer.innerHTML += xmlString;
  });
};

//send cart items to django view
document.getElementById("orderButton").onclick = () => {
  var myRequest = new XMLHttpRequest();
  myRequest.onreadystatechange = () => {
    if (this.readyState == 4 && this.status == 200) {
      // Response
      var response = this.responseText;
    } else {
      console.log("failed");
    }
  };
  myRequest.open("POST", "/order", true);
  var csrftoken = getCookie("csrftoken");
  myRequest.setRequestHeader(
    "Content-type",
    "application/x-www-form-urlencoded"
  );
  myRequest.setRequestHeader("X-CSRFToken", csrftoken);
  var data = { data: cart };
  myRequest.send(JSON.stringify(cart));
};

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      // Does this cookie string begin withthe name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
