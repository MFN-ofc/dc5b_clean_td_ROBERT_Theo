const fs = require( 'fs');
const data = [
{ id: 1, name: 'Philipps', power:40 , autonomy:'3 hours', energy: '4000GHz' },
{ id: 2, name: 'GreenWorks', power: 40, autonomy: '2 hours', energy: '40V' },
{ id: 3, name: 'Black+Decker', power: 20, autonomy: '1 hour', energy: '36V' },
{ id: 4, name: 'Honda', power: 25, autonomy: '1.5 hours', energy: 'Gasoline' },
{ id: 5, name: 'Toro', power: 30, autonomy: '2 hours', energy: 'Gasoline' },
{ id: 6, name: 'Makita', power: 40, autonomy: '3 hours', energy: '40V' },
{ id: 7, name: 'WORX', power: 20, autonomy: '1 hour', energy: '20V' },
{ id: 8, name: 'Craftsman', power: 35, autonomy: '2 hours', energy: 'Gasoline' },
{ id: 9, name: 'Snapper', power: 25, autonomy: '1.5 hours', energy: 'Gasoline' },
{ id: 10, name: 'Ego Power+', power: 40, autonomy: '3 hours', energy: '56V' },
{ id: 11, name: 'Kobalt', power: 20, autonomy: '1 hour', energy: '40V' },
{ id: 12, name: 'RYOBI', power: 30, autonomy: '2 hours', energy: '40V' },
{ id: 13, name: 'Cub Cadet', power: 25, autonomy: '1.5 hours', energy: 'Gasoline' },
{ id: 14, name: 'Briggs & Stratton', power: 40, autonomy: '3 hours', energy: 'Gasoline' },
{ id: 15, name: 'DEWALT', power: 20, autonomy: '1 hour', energy: '20V' },
{ id: 16, name: 'Poulan Pro', power: 35, autonomy: '2 hours', energy: 'Gasoline' },
{ id: 17, name: 'LawnMaster', power: 25, autonomy: '1.5 hours', energy: '40V' },
{ id: 18, name: 'Swisher', power: 40, autonomy: '3 hours', energy: 'Gasoline' },
{ id: 19, name: 'Ariens', power: 20, autonomy: '1 hour', energy: 'Gasoline' },
];

const writeStream = fs.createWriteStream('/Users/theorobert/Desktop/dc5_b_Robert_Theo/Node/exo2/data.csv');
writeStream.write('Id, Nom de la tondeuse, Puissance, Autonomie, Energie\n');
data.forEach( (row) => {
writeStream.write(`${row.id},${row.name},${row.power},${row.autonomy},${row.energy}\n`);
console.log(row.name);
});
writeStream.end();

