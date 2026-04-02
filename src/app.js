const express = require('express');
const ageRoutes = require('./routes/ageRoutes');

const app = express();
app.use(express.json());

app.use('/check_age', ageRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
