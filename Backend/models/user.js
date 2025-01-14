const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// User schema
const UserSchema = new Schema({
    userId: { type: String, required: true, unique: true },
    measurements: {
        height: { type: Number, required: true },
        weight: { type: Number, required: true },
        chest: { type: Number, required: true },
        waist: { type: Number, required: true },
        hip: { type: Number, required: true },
    },
    purchaseHistory: [
        {
            itemId: { type: String, required: true },
            size: { type: String, required: true },
            success: { type: Boolean, required: true },  // True if user kept the item, false if returned
        }
    ]
});

module.exports = User = mongoose.model('user', UserSchema);

