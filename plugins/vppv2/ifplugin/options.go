package ifplugin

import (
	"github.com/ligato/cn-infra/config"
	"github.com/ligato/cn-infra/logging"
	"github.com/ligato/vpp-agent/plugins/kvscheduler"
	linux_ifplugin "github.com/ligato/vpp-agent/plugins/linuxv2/ifplugin"
	"github.com/ligato/vpp-agent/plugins/govppmux"
)

// DefaultPlugin is a default instance of IfPlugin.
var DefaultPlugin = *NewPlugin()

// NewPlugin creates a new Plugin with the provides Options
func NewPlugin(opts ...Option) *IfPlugin {
	p := &IfPlugin{}

	p.PluginName = "vpp-ifplugin"
	p.Scheduler = &kvscheduler.DefaultPlugin
	p.LinuxIfPlugin = &linux_ifplugin.DefaultPlugin
	p.GoVppmux = &govppmux.DefaultPlugin

	for _, o := range opts {
		o(p)
	}

	if p.Log == nil {
		p.Log = logging.ForPlugin(p.String())
	}
	if p.Cfg == nil {
		p.Cfg = config.ForPlugin(p.String(),
			config.WithCustomizedFlag(config.FlagName(p.String()), "vpp-ifplugin.conf"),
		)
	}

	return p
}

// Option is a function that can be used in NewPlugin to customize Plugin.
type Option func(*IfPlugin)

// UseDeps returns Option that can inject custom dependencies.
func UseDeps(f func(*Deps)) Option {
	return func(p *IfPlugin) {
		f(&p.Deps)
	}
}
