#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i = 0;
  const length = list.length;
  let index = length - 1;

  for (index; index >= 0; index--) {
    newList[i] = list[index];
    i++;
  }
  return newList;
};
