import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import ResumeAnalyzer from './pages/ResumeAnalyzer';
import CoverLetterGenerator from './pages/CoverLetterGenerator';
import MockInterview from './pages/MockInterview';
import Dashboard from './pages/Dashboard';
import './App.css';

function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
    setLoading(false);
  }, []);

  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        <Navbar user={user} setUser={setUser} />
        
        <main className="container mx-auto px-4 py-8">
          {!loading && (
            <Routes>
              <Route path="/" element={<Home user={user} />} />
              <Route path="/resume-analyzer" element={<ResumeAnalyzer user={user} />} />
              <Route path="/cover-letter" element={<CoverLetterGenerator user={user} />} />
              <Route path="/mock-interview" element={<MockInterview user={user} />} />
              <Route path="/dashboard" element={<Dashboard user={user} />} />
            </Routes>
          )}
        </main>
      </div>
    </Router>
  );
}

export default App;
