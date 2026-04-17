import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { updateField, resetForm } from "../redux/interactionSlice";

const InteractionForm = () => {
  const dispatch = useDispatch();
  const form = useSelector((state) => state.interaction.form);
  const [success, setSuccess] = useState(false);

  const handleChange = (e) => {
    dispatch(updateField({ field: e.target.name, value: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://127.0.0.1:8000/interactions/", form);
      setSuccess(true);
      dispatch(resetForm());

      setTimeout(() => setSuccess(false), 3000);
    } catch (error) {
      if (error.response) {
        console.error("FastAPI Error Detail:", error.response.data.detail);
        alert(JSON.stringify(error.response.data.detail, null, 2)); 
      } else {
        console.error("Network Error:", error);
      }
    }
  };

  return (
    <div className="interaction-form-container">
      <h2>Record Preview</h2>
      <p className="form-subtitle">This shows a live look at the data the AI is managing.</p>
      <form onSubmit={handleSubmit} className="interaction-form">
        <label>HCP Name *</label>
        <input name="hcp_name" value={form.hcp_name} onChange={handleChange} required />

        <div className="form-row">
          <div>
            <label>Date *</label>
            <input type="date" name="interaction_date" value={form.interaction_date} onChange={handleChange} required />
          </div>
          <div>
            <label>Time *</label>
            <input type="time" name="interaction_time" value={form.interaction_time} onChange={handleChange} required />
          </div>
        </div>

        <label>Interaction Type *</label>
        <select name="interaction_type" value={form.interaction_type} onChange={handleChange} required>
          <option value="">Select</option>
          <option>In-person Visit</option>
          <option>Virtual Meeting</option>
          <option>Phone Call</option>
          <option>Conference</option>
        </select>

        <label>Attendees</label>
        <input name="attendees" value={form.attendees} onChange={handleChange} />

        <label>Topics Discussed</label>
        <textarea name="topics_discussed" value={form.topics_discussed} onChange={handleChange} />

        <label>Materials Shared</label>
        <textarea name="materials_shared" value={form.materials_shared} onChange={handleChange} />

        <label>Samples Distributed</label>
        <textarea name="samples_distributed" value={form.samples_distributed} onChange={handleChange} />

        <label>Observed/Inferred HCP Sentiment *</label>
        <div className="radio-group">
          <label>
            <input 
              type="radio" 
              name="sentiment" 
              value="Positive" 
              checked={form.sentiment === "Positive"} 
              onChange={handleChange} 
              required 
            /> Positive
          </label>
          <label>
            <input 
              type="radio" 
              name="sentiment" 
              value="Neutral" 
              checked={form.sentiment === "Neutral"} 
              onChange={handleChange} 
            /> Neutral
          </label>
          <label>
            <input 
              type="radio" 
              name="sentiment" 
              value="Negative" 
              checked={form.sentiment === "Negative"} 
              onChange={handleChange} 
            /> Negative
          </label>
        </div>

        <label>Outcomes</label>
        <textarea name="outcomes" value={form.outcomes} onChange={handleChange} />

        <label>Follow-up Actions</label>
        <textarea name="follow_up_actions" value={form.follow_up_actions} onChange={handleChange} />

        <button type="submit" className="submit-btn">Submit Interaction</button>

        {success && <div className="success-message">Interaction saved successfully!</div>}
      </form>
    </div>
  );
};

export default InteractionForm;