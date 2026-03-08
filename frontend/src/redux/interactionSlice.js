import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  form: {
    hcp_name: "",
    interaction_date: "",
    interaction_time: "",
    interaction_type: "",
    attendees: "",
    topics_discussed: "",
    materials_shared: "",
    samples_distributed: "",
    sentiment: "",
    outcomes: "",
    follow_up_actions: ""
  },
  chatMessages: []
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,
  reducers: {
    updateField: (state, action) => {
      const { field, value } = action.payload;
      state.form[field] = value;
    },
    resetForm: (state) => {
      state.form = initialState.form;
    },
    addMessage: (state, action) => {
      state.chatMessages.push(action.payload);
    }
  }
});

export const { updateField, resetForm, addMessage } = interactionSlice.actions;
export default interactionSlice.reducer;