let required = (propertyType) => {
  return (v) =>
    (v && v.length > 0) || `${propertyType} fehlt. Bitte eingeben. `;
};
let minLength = (propertyType, minLength) => {
  return (v) =>
    (v && v.length >= minLength) ||
    `${propertyType} zu kurz! Muss mindestens ${minLength} Zeichen lang sein.`;
};
let maxLength = (propertyType, maxLength) => {
  return (v) =>
    (v && v.length <= maxLength) ||
    `${propertyType} zu lang! Darf maximal ${maxLength} Zeichen umfassen. ${v}`;
};
let checkSelected = (propertyType) => {
  return (v) => (v && v != "") || `${propertyType} nicht ausgewählt!`;
};
let checkImage = (propertyType) => {
  return (value) =>
    !value ||
    value.size < 2000000 ||
    `Die Bildgröße sollte weniger als 2 MB betragen!`;
};

export default { required, minLength, maxLength, checkSelected, checkImage };
