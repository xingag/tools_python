//计算两个数的和
function add(num1, num2) {
    return num1 + num2;
}

//新增一个导出函数（node方式）
module.exports.init = function (arg1, arg2) {
    //调用函数
    console.log(add(arg1, arg2));
};