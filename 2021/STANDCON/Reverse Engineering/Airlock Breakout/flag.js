function part1(str1) {
    if (str1.length === 5) {
        arr = str1.split("");
        if (
            arr[0] === String.fromCharCode(51) &&
            arr[1] === String.fromCharCode(74) &&
            arr[2] === String.fromCharCode(51) &&
            arr[3] === String.fromCharCode(67) &&
            arr[4] === String.fromCharCode(55)
        )
            return true;
    }
}

function part2(str2) {
    if (str2.length === 4) {
        if (
            str2.charCodeAt(0) +
                2 * str2.charCodeAt(1) -
                3 * str2.charCodeAt(2) +
                4 * str2.charCodeAt(3) ===
                354 &&
            2 * str2.charCodeAt(0) +
                2 * str2.charCodeAt(1) -
                2 * str2.charCodeAt(2) +
                3 * str2.charCodeAt(3) ===
                383 &&
            3 * str2.charCodeAt(0) -
                2 * str2.charCodeAt(1) -
                4 * str2.charCodeAt(2) +
                str2.charCodeAt(3) ===
                -106 &&
            2 * Math.pow(str2.charCodeAt(0), 3) +
                3 * Math.pow(str2.charCodeAt(1), 2) -
                2 * Math.pow(str2.charCodeAt(2), 3) -
                4 * Math.pow(str2.charCodeAt(3), 2) ===
                59284
        )
            return true;
    }
}

function part3(str3, str4, str5, str6) {
    var magic = 0;
    for (var strs of [str3, str4, str5, str6]) {
        if (!/^[01347CFHKLNRUX]+$/g.test(strs)) return false;

        for (var i = 0; i < strs.length; i++) {
            magic = (magic << 3) + strs.charCodeAt(i) - magic;
        }
    }

    if (
        str3.length === 3 &&
        str4.length === 2 &&
        str5.length === 3 &&
        str6.length > 5 &&
        str3[0] === "0" &&
        str5[0] === "7" &&
        str3.charCodeAt(0) + str5.charCodeAt(0) - str6.charCodeAt(0) === 51 &&
        str3.charCodeAt(0) === str4.charCodeAt(0) &&
        str3.charCodeAt(2) - str3.charCodeAt(1) === -30 &&
        (str4.charCodeAt(1) / 7) * str5.charCodeAt(1) === 720 &&
        (str5.charCodeAt(0) + str5.charCodeAt(2) + 2) / 3 === 36 &&
        str6.charCodeAt(3) - str6.charCodeAt(2) === -6 &&
        str6.charCodeAt(2) * str6.charCodeAt(4) === 3936 &&
        magic === -859895409
    )
        return true;
}

function unlock(pwd) {
    var flagSplit = pwd.split("_");
    if (flagSplit.length !== 6) return false;

    if (part1(flagSplit[0])) console.log("Airlock 1 is opened");
    else return false;
    if (part2(flagSplit[1])) console.log("Airlock 2 is opened");
    else return false;
    if (part3(flagSplit[2], flagSplit[3], flagSplit[4], flagSplit[5]))
        console.log("Airlock 3 is opened");
    else return false;

    console.log(`Congratulations!\nFlag: STC{${pwd}}`);
}



// unknowns
var s32 = 0; var s52 = 0; var s62 = 0; var s65 = 0; var s66 = 0;

// known chars
var s31 = 48; var s41 = 48; var s51 = 55; var s53 = 51; var s61 = 52;

// list of possible chars
const possible_chars = "01347CFHKLNRUX";
const charlist = [];
for (var i in possible_chars) charlist.push(possible_chars.charCodeAt(i));
// charlist = [48, 49, 51, 52, 55, 67, 70, 72, 75, 76, 78, 82, 85, 88]

// list of possible str3 inputs
const strings3 = [];
for (var vals of charlist) {
  s32 = vals; var s33 = s32 - 30;
  if (charlist.includes(s33)) strings3.push(String.fromCharCode(s31,s32,s33));
}

// list of possible str4 inputs
const strings4 = [];
for (var vals of charlist) {
  var s42 = 5040/vals;
  if (charlist.includes(s42)) strings4.push(String.fromCharCode(s41,s42));
}

// list of possible str5 inputs
const strings5 = [];
for (var vals of charlist) {
  var s52 = 5040/vals;
  if (charlist.includes(s52)) strings5.push(String.fromCharCode(s51,s52,s53));
}

// list of possible str6 inputs
const strings6 = [];
for (var vals3 of charlist) {
  for (var vals2 of charlist) {
    for (var vals1 of charlist) {
      s62 = vals1; s65 = vals2; s66 = vals3;
      var s63 = 3936/s65; var s64 = -6*(s65 - 656)/s65;
      if (charlist.includes(s63) && charlist.includes(s64))
        strings6.push(String.fromCharCode(s61,s62,s63,s64,s65,s66));
    }
  }
}

var str1 = String.fromCharCode(51,74,51,67,55); // str1 = "3J3C7"
var str2 = String.fromCharCode(55,72,51,77);    // str2 = "7H3M"

const strings6_len7 = [];
for (var str6 of strings6)
  for (var chr of possible_chars)
    strings6_len7.push(str6+chr);

for (var str6 of strings6_len7)
  for (var str5 of strings5)
    for (var str4 of strings4)
      for (var str3 of strings3)
        if (part3(str3,str4,str5,str6))
          unlock(str1+"_"+str2+"_"+str3+"_"+str4+"_"+str5+"_"+str6)