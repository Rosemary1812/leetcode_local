//防抖
function debounce(dn, delay) {
  let timer = null;
  return function () {
    clearTimeout(timer);

    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}

// 节流
function throttle(fn, delay) {
  let lastTime = 0;
  return function () {
    const now = Date.now();
    if (now - lastTime >= interval) {
      lastTime = now;
      fn.apply(this, args);
    }
  };
}

// 发布订阅模式

class EventEmmiter {
  constructor() {
    this.arrayList = {};
  }
  on(name, fn) {
    if (!this.arrayList[name]) {
      this.arrayList[name] = [];
    }
    if (!this.arrayList[name].includes(fn)) {
      this.arrayList[name].push(fn);
    }
    return () => this.off(name, fn);
  }

  off(name, fn) {
    if (!this.arrayList[name]) {
      return;
    }
    const idx = this.arrayList[name].indexOf(fn);
    if (idx != -1) {
      this.arrayList[name].splice(idx, l);
    }
  }
  emit(name, ...args) {
    if (this.arrayList[name]) {
      return;
    }
    const tasks = [...this.arrayList[name]];
    for (const fn of tasks) {
      fn.call(this, ...args);
    }
  }
}

// promiseALL

function promiseALL(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let remaining = promises.length;
    if (!remaining) return resolve(results);
    promises.forEach((promise, idx) => {
      Promise.resolve(promsie)
        .then((value) => {
          results[idx] = value;
          remaining--;
          if (remaining === 0) {
            resolve(results);
          }
        })
        .catch(reject);
    });
  });
}

// PromiseAllSettled
function PromiseAllSettled(promises) {
  const wrappedPromiese = promises.map(
    promise.then(
      (value) => ({ status: "fulfilled", value }),
      (reason) => ({ status: "rejected", reason }),
    ),
  );
  return promiseALL(wrappedPromiese);
}

//new

function myNew(fn, ...args) {
  if (Object.prototype.toString.call(fn) !== "[object Function") {
    return "Error";
  }
  const obj = {};
  obj.__proto__ = Object.create(fn.prototype);
  let ret = fn.call(obj, ...args);
  return ret instanceof Object ? ret : obj;
}

// instance of

function instanceOf(left,right){
  const prototype=right.prototype
  let proto=Object.getPrototypeOf(left)
  while(true){
    if(proto===null)return false
    if(proto===prototype)return true
    proto=Object.getPrototypeOf(proto)
  }
}

// call&apply
Function.prototype.call = function () {
  let [thisArg, ...args] = [...arguments];
  thisArg = Object(thisArg) || window;
  let fn = Symbol()
  thisArg[fn] = this
  let result = thisArg[fn](...args);
  delete thisArg[fn];
  return result
}
// bind
Function.prototype.mybind = function (context, ...args) {
  return (...rest)={
    return this.call(context,...args,...rest)
  }
}

// curry
const curry = (fn, ...args) => {
  if (args.length >= fn.length) {
    return fn(...args)
  }
  return (...rest) => {
    return curry(fn,...args,...rest)
  }
}

// flat
const flat = (arr, depth = 1) => {
  let res = []
  for (let i = 0; i < arr.length; i++){
    if (Array.isArray(arr[i]) && depth > 0) {
      res=res.concat(flat(arr[i],depth-1))
    } else {
      res.push(arr[i])
    }
  }
  return res
}

// map
Array.prototype.map = function (fn) {
  const res = []
  for (let i = 0; i < this.length; i++){
    res.push(fn(this[i],i,this))
  }
  return res;
}
// filter
Array.prototype.filter = function (fn) {
  const res = []
  for (let i = 0; i < this.length; i++){
    if (fn(this[i].j, this)) {
      res.push(this[i])
    }
  }
  return res;
}

Array.prototype.reduce = function (fn, value) {
  let res, start = 0
  if (arguments.length !== 1) {
    res = value;
  } else {
    res = this[0];
    start=1
  }
  for (let i = 0; i < this.length; i++){
    res=fn(res,this[i],i,this)
  }
  return res;
}
