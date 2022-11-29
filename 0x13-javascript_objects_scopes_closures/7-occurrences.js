#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let i = 0;
  const length = list.length;

  for (i; i < length; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return (count);
};
