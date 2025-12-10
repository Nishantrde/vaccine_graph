"""
Interactive Dashboard for Vaccine Awareness Simulation

Provides a command-line interactive interface for exploring
different scenarios and parameter combinations.
"""

import sys
from vaccine_awareness_simulation import (
    VaccineAwarenessSimulation,
    SimulationParameters,
    compare_scenarios
)
from advanced_analysis import run_advanced_analysis


class InteractiveDashboard:
    """
    Command-line interface for exploring the simulation
    """
    
    def __init__(self):
        self.params = SimulationParameters()
        
    def display_menu(self):
        """Display main menu"""
        print("\n" + "=" * 80)
        print("VACCINE AWARENESS SIMULATION - INTERACTIVE DASHBOARD")
        print("=" * 80)
        print("\nSelect an option:")
        print("  1. Run standard scenario comparison")
        print("  2. Run custom simulation")
        print("  3. Modify simulation parameters")
        print("  4. Run advanced analysis suite")
        print("  5. View current parameters")
        print("  6. Quick sensitivity test")
        print("  0. Exit")
        print("-" * 80)
        
    def view_parameters(self):
        """Display current parameters"""
        print("\n" + "=" * 80)
        print("CURRENT SIMULATION PARAMETERS")
        print("=" * 80)
        
        print("\nPopulation:")
        print(f"  Total population: {self.params.population:,}")
        print(f"  Simulation duration: {self.params.time_days / 365:.1f} years")
        
        print("\nDisease Characteristics:")
        print(f"  Transmission rate (β): {self.params.beta}")
        print(f"  Incubation rate (σ): {self.params.sigma} (latent period: {1/self.params.sigma:.1f} days)")
        print(f"  Recovery rate (γ): {self.params.gamma} (infectious period: {1/self.params.gamma:.1f} days)")
        print(f"  Basic reproduction number (R₀): {self.params.beta / self.params.gamma:.2f}")
        print(f"  Case fatality rate: {self.params.disease_mortality:.2%}")
        
        print("\nVaccine Parameters:")
        print(f"  Vaccine efficacy: {self.params.vaccine_efficacy:.0%}")
        print(f"  Baseline coverage: {self.params.vaccine_coverage_baseline:.0%}")
        print(f"  Baseline hesitancy: {self.params.vaccine_hesitancy_baseline:.0%}")
        
        print("\nAwareness & Behavior:")
        print(f"  Media campaign strength: {self.params.media_campaign_strength}")
        print(f"  Awareness decay rate: {self.params.awareness_decay_rate}")
        print(f"  Social influence strength: {self.params.social_influence_strength}")
        print(f"  Disease risk perception: {self.params.risk_perception_disease}")
        print(f"  Vaccine risk perception: {self.params.risk_perception_vaccine}")
        
        input("\nPress Enter to continue...")
        
    def modify_parameters(self):
        """Allow user to modify parameters"""
        print("\n" + "=" * 80)
        print("MODIFY PARAMETERS")
        print("=" * 80)
        
        print("\nSelect parameter category to modify:")
        print("  1. Population & Time")
        print("  2. Disease characteristics")
        print("  3. Vaccine parameters")
        print("  4. Awareness & campaigns")
        print("  0. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice: "))
            
            if choice == 1:
                self._modify_population()
            elif choice == 2:
                self._modify_disease()
            elif choice == 3:
                self._modify_vaccine()
            elif choice == 4:
                self._modify_awareness()
                
        except (ValueError, KeyboardInterrupt):
            print("\nInvalid input. Returning to menu.")
    
    def _modify_population(self):
        """Modify population parameters"""
        try:
            pop = int(input(f"\nPopulation [{self.params.population:,}]: ") or self.params.population)
            years = float(input(f"Simulation years [{self.params.time_days/365:.1f}]: ") or self.params.time_days/365)
            
            self.params.population = pop
            self.params.time_days = int(years * 365)
            print("✓ Parameters updated")
        except ValueError:
            print("✗ Invalid input")
    
    def _modify_disease(self):
        """Modify disease parameters"""
        try:
            beta = float(input(f"\nTransmission rate β [{self.params.beta}]: ") or self.params.beta)
            mortality = float(input(f"Case fatality rate [{self.params.disease_mortality}]: ") or self.params.disease_mortality)
            
            self.params.beta = beta
            self.params.disease_mortality = mortality
            print(f"✓ Parameters updated (New R₀: {beta / self.params.gamma:.2f})")
        except ValueError:
            print("✗ Invalid input")
    
    def _modify_vaccine(self):
        """Modify vaccine parameters"""
        try:
            efficacy = float(input(f"\nVaccine efficacy 0-1 [{self.params.vaccine_efficacy}]: ") or self.params.vaccine_efficacy)
            coverage = float(input(f"Baseline coverage 0-1 [{self.params.vaccine_coverage_baseline}]: ") or self.params.vaccine_coverage_baseline)
            hesitancy = float(input(f"Baseline hesitancy 0-1 [{self.params.vaccine_hesitancy_baseline}]: ") or self.params.vaccine_hesitancy_baseline)
            
            self.params.vaccine_efficacy = max(0, min(1, efficacy))
            self.params.vaccine_coverage_baseline = max(0, min(1, coverage))
            self.params.vaccine_hesitancy_baseline = max(0, min(1, hesitancy))
            print("✓ Parameters updated")
        except ValueError:
            print("✗ Invalid input")
    
    def _modify_awareness(self):
        """Modify awareness parameters"""
        try:
            campaign = float(input(f"\nCampaign strength 0-1 [{self.params.media_campaign_strength}]: ") or self.params.media_campaign_strength)
            decay = float(input(f"Awareness decay rate [{self.params.awareness_decay_rate}]: ") or self.params.awareness_decay_rate)
            social = float(input(f"Social influence 0-1 [{self.params.social_influence_strength}]: ") or self.params.social_influence_strength)
            
            self.params.media_campaign_strength = max(0, min(1, campaign))
            self.params.awareness_decay_rate = max(0, decay)
            self.params.social_influence_strength = max(0, min(1, social))
            print("✓ Parameters updated")
        except ValueError:
            print("✗ Invalid input")
    
    def run_custom_simulation(self):
        """Run a single custom simulation"""
        print("\n" + "=" * 80)
        print("CUSTOM SIMULATION")
        print("=" * 80)
        
        print("\nSelect scenario type:")
        print("  1. Baseline (moderate campaigns)")
        print("  2. Aggressive campaign")
        print("  3. No intervention")
        print("  4. Targeted (threshold-based)")
        
        try:
            choice = int(input("\nEnter choice: "))
            scenario_map = {
                1: "baseline",
                2: "aggressive_campaign",
                3: "no_intervention",
                4: "targeted"
            }
            
            if choice not in scenario_map:
                print("Invalid choice")
                return
            
            scenario = scenario_map[choice]
            
            print(f"\nRunning {scenario} scenario...")
            print("-" * 80)
            
            sim = VaccineAwarenessSimulation(self.params)
            history = sim.run_simulation(scenario)
            metrics = sim.calculate_metrics()
            
            print("\nRESULTS:")
            print("-" * 80)
            for key, value in metrics.items():
                print(f"  {key.replace('_', ' ').title()}: {value}")
            
            # Simple visualization option
            visualize = input("\nGenerate visualization? (y/n): ").lower()
            if visualize == 'y':
                from vaccine_awareness_simulation import visualize_results
                import matplotlib.pyplot as plt
                
                visualize_results({scenario: history}, self.params)
                plt.show()
            
        except (ValueError, KeyboardInterrupt):
            print("\nOperation cancelled")
    
    def quick_sensitivity_test(self):
        """Run a quick sensitivity test on one parameter"""
        print("\n" + "=" * 80)
        print("QUICK SENSITIVITY TEST")
        print("=" * 80)
        
        print("\nTest sensitivity to:")
        print("  1. Campaign strength")
        print("  2. Vaccine hesitancy")
        print("  3. Social influence")
        
        try:
            choice = int(input("\nEnter choice: "))
            
            param_map = {
                1: ('media_campaign_strength', 'Campaign Strength', [0.0, 0.3, 0.6, 1.0]),
                2: ('vaccine_hesitancy_baseline', 'Vaccine Hesitancy', [0.05, 0.15, 0.30, 0.45]),
                3: ('social_influence_strength', 'Social Influence', [0.0, 0.3, 0.6, 1.0])
            }
            
            if choice not in param_map:
                print("Invalid choice")
                return
            
            param_name, param_label, values = param_map[choice]
            
            print(f"\nTesting {param_label} at values: {values}")
            print("-" * 80)
            
            results = []
            for value in values:
                # Create modified params
                test_params = SimulationParameters()
                for attr in dir(self.params):
                    if not attr.startswith('_'):
                        setattr(test_params, attr, getattr(self.params, attr))
                
                setattr(test_params, param_name, value)
                
                # Run simulation
                sim = VaccineAwarenessSimulation(test_params)
                sim.run_simulation("baseline")
                metrics = sim.calculate_metrics()
                
                results.append((value, metrics['total_deaths'], metrics['vaccination_coverage']))
                print(f"  {param_label} = {value:.2f}: {metrics['total_deaths']:,} deaths, "
                      f"{metrics['vaccination_coverage']} coverage")
            
            print("\n" + "-" * 80)
            best = min(results, key=lambda x: x[1])
            print(f"Optimal value: {best[0]:.2f} (fewest deaths: {best[1]:,})")
            
        except (ValueError, KeyboardInterrupt):
            print("\nOperation cancelled")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main interaction loop"""
        while True:
            try:
                self.display_menu()
                choice = input("Enter choice: ").strip()
                
                if choice == '0':
                    print("\nExiting simulation. Stay safe!")
                    break
                elif choice == '1':
                    compare_scenarios()
                    input("\nPress Enter to continue...")
                elif choice == '2':
                    self.run_custom_simulation()
                elif choice == '3':
                    self.modify_parameters()
                elif choice == '4':
                    run_advanced_analysis()
                    input("\nPress Enter to continue...")
                elif choice == '5':
                    self.view_parameters()
                elif choice == '6':
                    self.quick_sensitivity_test()
                else:
                    print("\n✗ Invalid choice. Please try again.")
                    
            except KeyboardInterrupt:
                print("\n\nExiting simulation. Stay safe!")
                break
            except Exception as e:
                print(f"\n✗ Error: {e}")
                print("Please try again.")


def main():
    """Entry point for interactive dashboard"""
    dashboard = InteractiveDashboard()
    dashboard.run()


if __name__ == "__main__":
    main()
