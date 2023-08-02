const fs = require('fs');
const path = require('path');

const notesFilePath = path.join(__dirname, 'notes.json');

const loadNotes = () => {
  try {
    const dataBuffer = fs.readFileSync(notesFilePath);
    const dataJSON = dataBuffer.toString();
    return JSON.parse(dataJSON);
  } catch (error) {
    return [];
  }
};

const saveNotes = notes => {
  const dataJSON = JSON.stringify(notes);
  fs.writeFileSync(notesFilePath, dataJSON);
};

const addNote = (title, body) => {
  const notes = loadNotes();
  const duplicateNote = notes.find(note => note.title === title);

  if (!duplicateNote) {
    notes.push({ title, body });
    saveNotes(notes);
    console.log('Note added successfully.');
  } else {
    console.log('Note already exists.');
  }
};

const listNotes = () => {
  const notes = loadNotes();
  console.log('Your notes:');
  notes.forEach(note => {
    console.log(note.title);
  });
};

const readNote = title => {
  const notes = loadNotes();
  const note = notes.find(note => note.title === title);

  if (note) {
    console.log(`Title: ${note.title}`);
    console.log(`Body: ${note.body}`);
  } else {
    console.log('Note not found.');
  }
};

const removeNote = title => {
  const notes = loadNotes();
  const notesToKeep = notes.filter(note => note.title !== title);

  if (notes.length > notesToKeep.length) {
    saveNotes(notesToKeep);
    console.log('Note removed successfully.');
  } else {
    console.log('Note not found.');
  }
};

module.exports = {
  addNote,
  listNotes,
  readNote,
  removeNote
};
