#include <cmath>
#include <cstring>
#include <stdexcept>
// Gotran generated C/C++ code for the "hodgkin_huxley_squid_axon_1952" model

// Init state values
void init_state_values(double* states)
{
  states[0] = 0.05; // m;
  states[1] = 0.6; // h;
  states[2] = 0.325; // n;
  states[3] = -75; // V;
}

// Default parameter values
void init_parameters_values(double* parameters)
{
  parameters[0] = 120; // g_Na;
  parameters[1] = 36; // g_K;
  parameters[2] = 0.3; // g_L;
  parameters[3] = 1; // Cm;
  parameters[4] = -75; // E_R;
}

// State index
int state_index(const char name[])
{
  // State names
  char names[][2] = {"m", "h", "n", "V"};

  int i;
  for (i=0; i<4; i++)
  {
    if (strcmp(names[i], name)==0)
    {
      return i;
    }
  }
  return -1;
}

// Parameter index
int parameter_index(const char name[])
{
  // Parameter names
  char names[][5] = {"g_Na", "g_K", "g_L", "Cm", "E_R"};

  int i;
  for (i=0; i<5; i++)
  {
    if (strcmp(names[i], name)==0)
    {
      return i;
    }
  }
  return -1;
}

// Compute the right hand side of the hodgkin_huxley_squid_axon_1952 ODE
void rhs(const double* states, const double t, const double* parameters,
  double* values)
{

  // Assign states
  const double m = states[0];
  const double h = states[1];
  const double n = states[2];
  const double V = states[3];

  // Assign parameters
  const double g_Na = parameters[0];
  const double g_K = parameters[1];
  const double g_L = parameters[2];
  const double Cm = parameters[3];
  const double E_R = parameters[4];

  // Expressions for the Sodium channel component
  const double E_Na = 115. + E_R;
  const double i_Na = g_Na*(m*m*m)*(V - E_Na)*h;

  // Expressions for the m gate component
  const double alpha_m = (-5.0 - 0.1*V)/(-1. + std::exp(-5. - V/10.));
  const double beta_m = 4.*std::exp(-25./6. - V/18.);
  values[0] = (1. - m)*alpha_m - beta_m*m;

  // Expressions for the h gate component
  const double alpha_h = 0.07*std::exp(-15./4. - V/20.);
  const double beta_h = 1.0/(1. + std::exp(-9./2. - V/10.));
  values[1] = -beta_h*h + (1. - h)*alpha_h;

  // Expressions for the Potassium channel component
  const double E_K = -12. + E_R;
  const double i_K = g_K*std::pow(n, 4.)*(-E_K + V);

  // Expressions for the n gate component
  const double alpha_n = (-0.65 - 0.01*V)/(-1. + std::exp(-13./2. - V/10.));
  const double beta_n = 0.125*std::exp(15./16. + V/80.);
  values[2] = -beta_n*n + (1. - n)*alpha_n;

  // Expressions for the Leakage current component
  const double E_L = 10.613 + E_R;
  const double i_L = g_L*(V - E_L);

  // Expressions for the Membrane component
  const double i_Stim = ((t <= 10.5) && (t >= 10.) ? 20. : 0.);
  values[3] = (-i_L - i_K + i_Stim - i_Na)/Cm;
}

// Compute a forward step using the rush larsen algorithm to the
// hodgkin_huxley_squid_axon_1952 ODE
void forward_rush_larsen(double* states, const double t, const double dt,
  const double* parameters)
{

  // Assign states
  const double m = states[0];
  const double h = states[1];
  const double n = states[2];
  const double V = states[3];

  // Assign parameters
  const double g_Na = parameters[0];
  const double g_K = parameters[1];
  const double g_L = parameters[2];
  const double Cm = parameters[3];
  const double E_R = parameters[4];

  // Expressions for the Sodium channel component
  const double E_Na = 115. + E_R;
  const double i_Na = g_Na*(m*m*m)*(V - E_Na)*h;

  // Expressions for the m gate component
  const double alpha_m = (-5.0 - 0.1*V)/(-1. + std::exp(-5. - V/10.));
  const double beta_m = 4.*std::exp(-25./6. - V/18.);
  const double dm_dt = (1. - m)*alpha_m - beta_m*m;
  const double dm_dt_linearized = -beta_m - alpha_m;
  states[0] = (std::fabs(dm_dt_linearized) > 1.0e-8 ? (-1.0 +
    std::exp(dt*dm_dt_linearized))*dm_dt/dm_dt_linearized : dt*dm_dt) + m;

  // Expressions for the h gate component
  const double alpha_h = 0.07*std::exp(-15./4. - V/20.);
  const double beta_h = 1.0/(1. + std::exp(-9./2. - V/10.));
  const double dh_dt = -beta_h*h + (1. - h)*alpha_h;
  const double dh_dt_linearized = -beta_h - alpha_h;
  states[1] = h + (std::fabs(dh_dt_linearized) > 1.0e-8 ? (-1.0 +
    std::exp(dt*dh_dt_linearized))*dh_dt/dh_dt_linearized : dt*dh_dt);

  // Expressions for the Potassium channel component
  const double E_K = -12. + E_R;
  const double i_K = g_K*std::pow(n, 4.)*(-E_K + V);

  // Expressions for the n gate component
  const double alpha_n = (-0.65 - 0.01*V)/(-1. + std::exp(-13./2. - V/10.));
  const double beta_n = 0.125*std::exp(15./16. + V/80.);
  const double dn_dt = -beta_n*n + (1. - n)*alpha_n;
  const double dn_dt_linearized = -alpha_n - beta_n;
  states[2] = (std::fabs(dn_dt_linearized) > 1.0e-8 ? (-1.0 +
    std::exp(dt*dn_dt_linearized))*dn_dt/dn_dt_linearized : dt*dn_dt) + n;

  // Expressions for the Leakage current component
  const double E_L = 10.613 + E_R;
  const double i_L = g_L*(V - E_L);

  // Expressions for the Membrane component
  const double i_Stim = ((t <= 10.5) && (t >= 10.) ? 20. : 0.);
  const double dV_dt = (-i_L - i_K + i_Stim - i_Na)/Cm;
  states[3] = V + dt*dV_dt;
}

// Compute a forward step using the explicit Euler algorithm to the
// hodgkin_huxley_squid_axon_1952 ODE
void forward_explicit_euler(double* states, const double t, const double dt,
  const double* parameters)
{

  // Assign states
  const double m = states[0];
  const double h = states[1];
  const double n = states[2];
  const double V = states[3];

  // Assign parameters
  const double g_Na = parameters[0];
  const double g_K = parameters[1];
  const double g_L = parameters[2];
  const double Cm = parameters[3];
  const double E_R = parameters[4];

  // Expressions for the Sodium channel component
  const double E_Na = 115. + E_R;
  const double i_Na = g_Na*(m*m*m)*(V - E_Na)*h;

  // Expressions for the m gate component
  const double alpha_m = (-5.0 - 0.1*V)/(-1. + std::exp(-5. - V/10.));
  const double beta_m = 4.*std::exp(-25./6. - V/18.);
  const double dm_dt = (1. - m)*alpha_m - beta_m*m;
  states[0] = dt*dm_dt + m;

  // Expressions for the h gate component
  const double alpha_h = 0.07*std::exp(-15./4. - V/20.);
  const double beta_h = 1.0/(1. + std::exp(-9./2. - V/10.));
  const double dh_dt = -beta_h*h + (1. - h)*alpha_h;
  states[1] = h + dt*dh_dt;

  // Expressions for the Potassium channel component
  const double E_K = -12. + E_R;
  const double i_K = g_K*std::pow(n, 4.)*(-E_K + V);

  // Expressions for the n gate component
  const double alpha_n = (-0.65 - 0.01*V)/(-1. + std::exp(-13./2. - V/10.));
  const double beta_n = 0.125*std::exp(15./16. + V/80.);
  const double dn_dt = -beta_n*n + (1. - n)*alpha_n;
  states[2] = n + dt*dn_dt;

  // Expressions for the Leakage current component
  const double E_L = 10.613 + E_R;
  const double i_L = g_L*(V - E_L);

  // Expressions for the Membrane component
  const double i_Stim = ((t <= 10.5) && (t >= 10.) ? 20. : 0.);
  const double dV_dt = (-i_L - i_K + i_Stim - i_Na)/Cm;
  states[3] = V + dt*dV_dt;
}
